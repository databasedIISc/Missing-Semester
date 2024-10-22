import os
import hashlib
import argparse
import json
from typing import Union, List, Dict
import pickle

# Define types
Blob = bytes
Tree = Dict[str, Union['Tree', Blob]]
Object = Union[Blob, Tree, 'Commit']

class Commit:
    def __init__(self, parents: List['Commit'], author: str, message: str, snapshot: Tree):
        """A commit consists of parents, metadata (author, message), and a snapshot (tree)."""
        self.parents = parents 
        self.author = author
        self.message = message
        self.snapshot = snapshot

def sha1(data: Union[Blob, str]) -> str:
    """Hash objects using SHA1."""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha1(data).hexdigest()

def store(obj: Object) -> str:
    """Store an object and return its ID."""
    obj_data = pickle.dumps(obj)
    
    obj_id = sha1(obj_data)  # Compute SHA-1 hash of the object
    
    # Store the object in the `.smallgit/objects` directory
    obj_path = f".smallgit/objects/{obj_id}"

    with open(obj_path, "wb") as f:
        f.write(obj_data)

    return obj_id

def load(obj_id: str) -> Object:
    """Load an object by its ID."""
    if os.path.exists(f".smallgit/objects/{obj_id}"):
        with open(f".smallgit/objects/{obj_id}", "rb") as f:
            obj_data = f.read()
        
        if obj_id == sha1(obj_data):
            return pickle.loads(obj_data)                
        
        raise ValueError("Corrupted object data")
    
    raise FileNotFoundError("Object not found")

def create_blob(file_content: str) -> str:
    """Create and store a blob from file content (as a string)."""
    blob = file_content.encode()
    blob_id = store(blob)
    return blob_id

def create_tree(entries: Dict[str, Union[Blob, Tree]]) -> str:
    """Create and store a tree (directory structure)."""
    tree = entries
    tree_id = store(tree)
    return tree_id

def create_commit(parents: List[Commit], author: str, message: str, snapshot: Tree) -> str:
    """Create and store a commit object."""
    commit = Commit(parents, author, message, snapshot)
    commit_id = store(commit)
    return commit_id

def init():
    """Initialize a SmallGit repository."""
    if os.path.exists(".smallgit"):
        print("SmallGit repository already exists.")
        return
    
    os.makedirs(".smallgit")
    os.makedirs(".smallgit/objects")
    os.makedirs(".smallgit/refs/heads")
    with open(".smallgit/HEAD", "w") as f:
        f.write("ref: refs/heads/main")  # Initial branch is 'main'
    
    print("SmallGit repository initialized.")

def get_current_branch():
    """Get the current branch by reading the .smallgit/HEAD file."""
    with open(".smallgit/HEAD", "r") as f:
        ref = f.read().strip()
    return ref.split(": ")[1].split("/")[-1]  # Extract branch name

def add(files):
    """Stage files as blobs for commit."""
    index = {}
    for file in files:
        # 'file' can be a file path or a directory path (to add all files in the directory)
        if os.path.isdir(file):
            for root, _, filenames in os.walk(file):
                for filename in filenames:
                    if ".smallgit" in root:
                        continue
                    filepath = os.path.join(root, filename)
                    with open(filepath, "r") as f:
                        content = f.read()
                    blob_id = create_blob(content)
                    index[filepath] = blob_id
        else:      
            if os.path.exists(file):
                # ignore files in .smallgit directory
                if ".smallgit/" in file:
                    continue
                with open(file, "r") as f:
                    content = f.read()
                blob_id = create_blob(content)  # Create blob for file content
                index[file] = blob_id  # Track the blob ID for each file
            else:
                print(f"File '{file}' not found.")
                return
    
    # Save the index (staging area) to a file
    with open(".smallgit/index", "w") as index_file:
        index_file.write(json.dumps(index))  # Store the staged files (blobs)

    print(f"Staged files: {', '.join(files)}")

def commit(message):
    """Commit the staged files."""
    if not os.path.exists(".smallgit/index"):
        print("Nothing to commit.")
        return
    
    # Read the index (staged files)
    with open(".smallgit/index", "r") as index_file:
        staged_files = json.loads(index_file.read())
    
    # Create a tree (snapshot) from the staged files
    snapshot_tree = {filename: blob_id for filename, blob_id in staged_files.items()}
    
    # Get the current branch and any parent commit
    branch = get_current_branch()
    parent_commit = None
    if os.path.exists(f".smallgit/refs/heads/{branch}"):
        with open(f".smallgit/refs/heads/{branch}", "r") as f:
            parent_commit_id = f.read().strip()
            parent_commit = load(parent_commit_id)

    # Create the new commit object
    new_commit_id = create_commit(
        parents=[parent_commit] if parent_commit else [],
        author="Mrigank <mrigankp@iisc.ac.in>",
        message=message,
        snapshot=snapshot_tree
    )

    # Update the branch reference with the new commit ID
    with open(f".smallgit/refs/heads/{branch}", "w") as f:
        f.write(new_commit_id)
    
    # Clear the index (staging area)
    os.remove(".smallgit/index")

    print(f"Committed with message: {message} (Commit ID: {new_commit_id})")

def status():
    """Show the status of the working directory."""
    if os.path.exists(".smallgit/index"):
        print("Changes staged for commit:")
        with open(".smallgit/index", "r") as index_file:
            staged_files = json.loads(index_file.read())
            staged_file_items = list(staged_files.keys())
            for filename in staged_files:
                print(f"\t{filename}")
    else:
        print("No changes staged for commit.")
        staged_file_items = []

    # changes not staged for commit (modified files)
    print("\nChanges not staged for commit (modified files):")
    for root, _, filenames in os.walk("."):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            if ".smallgit" in filepath:
                continue

            # the path string may differ due to OS differences or starting with './'
            if filepath.startswith("./") or filepath.startswith(".\\"):
                filepath = filepath[2:]

            for staged_file in staged_file_items:
                if staged_file.startswith("./") or staged_file.startswith(".\\"):
                    staged_file = staged_file[2:]
                if filepath == staged_file:
                    break
            else:
                with open(filepath, "r") as f:
                    content = f.read()
                blob_id = create_blob(content)
                
                # Compare the blob ID with the blob ID in the HEAD commit
                branch = get_current_branch()
                if os.path.exists(f".smallgit/refs/heads/{branch}"):
                    with open(f".smallgit/refs/heads/{branch}", "r") as f:
                        commit_id = f.read().strip()
                        commit = load(commit_id)
                        snapshot_blob = commit.snapshot[filepath]
                        if filepath in commit.snapshot and snapshot_blob != blob_id:
                            print(f"\t{filepath}")
                else:
                    print(f"\t{filepath}") # all files are new

def log():
    """Show the commit history of the current branch."""
    branch = get_current_branch()
    if not os.path.exists(f".smallgit/refs/heads/{branch}"):
        print(f"No commits on branch '{branch}'.")
        return

    commit_id = ""
    with open(f".smallgit/refs/heads/{branch}", "r") as f:
        commit_id = f.read().strip()

    # Traverse commit history and print log
    while commit_id:
        commit = load(commit_id)
        print(f"Commit {commit_id} by {commit.author}")
        print(f"\n    {commit.message}\n")
        if commit.parents:
            commit_id = store(commit.parents[0])  # Follow the first parent commit
        else:
            break

def checkout(commit):
    """
    Switch to the specified commit.
    Allow using 'HEAD' to switch to the latest commit on the current branch.
    """
    if commit == "HEAD":
        branch = get_current_branch()
        if os.path.exists(f".smallgit/refs/heads/{branch}"):
            with open(f".smallgit/refs/heads/{branch}", "r") as f:
                commit = f.read().strip()
        else:
            print(f"Branch '{branch}' does not exist.")
    
    # Load the commit object
    commit_obj = load(commit)
    
    # Restore the files from the commit snapshot
    for filename, obj_id in commit_obj.snapshot.items():
        content = load(obj_id).decode()
        
        os.makedirs("./" + os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(content)
    
    print(f"Switched to commit {commit}.")

def diff():
    """Show differences between the working directory and the staged area."""
    if not os.path.exists(".smallgit/index"):
        print("No changes to show.")
        return
    
    print("Differences between staged and working directory:")
    with open(".smallgit/index", "r") as index_file:
        staged_files = json.loads(index_file.read())
        for filename, blob_id in staged_files.items():
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    content = f.read()
                working_blob_id = create_blob(content)
                if working_blob_id != blob_id:
                    print(f"\t{filename} has changed.")
            else:
                print(f"\t{filename} is missing.")

def main():
    """CLI Interface for SmallGit."""
    parser = argparse.ArgumentParser(description="SmallGit: A Simple Git Implementation")
    
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Initialize a new repository")
    subparsers.add_parser("status", help="Show the status of the repository")

    add_parser = subparsers.add_parser("add", help="Add files to the staging area")
    add_parser.add_argument("files", nargs="+", help="Files to add")

    commit_parser = subparsers.add_parser("commit", help="Commit the staged changes")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")

    subparsers.add_parser("log", help="Show commit logs")

    checkout_parser = subparsers.add_parser("checkout", help="Switch to a commit")
    checkout_parser.add_argument("commit", help="Commit to switch to")

    subparsers.add_parser("diff", help="Show differences between the working directory and the index")

    args = parser.parse_args()

    if args.command == "init":
        init()
    elif args.command == "status":
        status()
    elif args.command == "add":
        add(args.files)
    elif args.command == "commit":
        commit(args.message)
    elif args.command == "log":
        log()
    elif args.command == "checkout":
        checkout(args.commit)
    elif args.command == "diff":
        diff()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
