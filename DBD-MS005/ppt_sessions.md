---
title: Missing Semester DBD005
author: Anirudh Gupta
sub_title: Vim & Terminal Multiplexer
theme:
  name: catppuccin-mocha
  override:
  footer:
    style: template
    left: "Anirudh Gupta"
    middle: "Introduction to Vim & Terminal Multiplexer"
    right: "{current_slide} / {total_slides}"
---

# Before Starting Introduction

<!-- pause-->

```
This will be the last Missing Semester Session
```

<!-- pause-->

What we have learnt -

<!-- pause-->

- Shell and Terminal
<!-- pause-->
- Debugging and Testing
<!-- pause-->
- Git
<!-- pause-->
- OOP
<!-- pause-->
- And today `VIM & Terminal Multiplexer`

<!-- pause-->

# What is Vim?

<!-- pause-->

All the instructors of this class use Vim as their editor. Vim has a rich history; it originated from the `Vi editor (1976)`, and it’s still being developed today.

Vim has some really neat ideas behind it, and for this reason, lots of tools support a Vim emulation mode (for example, People have installed Vim emulation for `VS code`, `shell`, `tmux`, `Obsidian`, and `vim bindings for even Google`, etc.). Vim is probably worth learning even if you finally end up switching to some other text editor.

<!-- end_slide-->

# Philosophy of Vim

<!-- pause-->

When programming, you spend most of your time reading/editing, not writing. For this reason, Vim is a modal editor:

<!-- pause-->

- It has different modes for inserting text vs manipulating text.
<!-- pause-->
- Vim is programmable (with Vimscript and also other languages like Python), and Vim’s interface itself is a programming language: `keystrokes (with mnemonic names) are commands`, and these commands are composable.
<!-- pause-->
- Vim avoids the use of the mouse, because `it’s too slow`; Vim even avoids using the `arrow keys` because it requires `too much movement`.
<!-- pause-->

The end result is an editor that can match the speed at which you think.

<!-- pause-->
<!-- pause-->

# Why Use Vim?

<!-- pause-->

- **Efficiency**: Vim's modal editing and powerful commands allow for quick and efficient text manipulation.
<!-- pause-->
- **Customizability**: Vim can be customized extensively using .vimrc configuration files.
<!-- pause-->
- **Ubiquity**: Vim is available on almost all UNIX systems and many other platforms.

<!-- end_slide-->

# Vim Modes

<!-- pause-->

- **Normal mode**: For navigation and manipulation
- **Insert mode**: For inserting text
- **Visual mode**: For selecting text
- **Command mode**: For executing commands
<!-- pause-->

## Normal Mode

This mode is the default mode in Vim. You can navigate through the text, delete, copy, paste, and perform other operations in this mode.

<!-- pause-->

## Insert Mode

In this mode, you can insert text into the file. You can enter insert mode by pressing `i` in normal mode.

<!-- pause-->

## Visual Mode

In this mode, you can select text by moving the cursor. You can enter visual mode by pressing `v` in normal mode.

- `v`: Start visual mode
- `V`: Start visual line mode
- `Ctrl-v`: Start visual block mode

<!--end_slide-->

# Basic Vim Commands

<!-- pause-->

## Insert and Exit Modes

- `i`: Enter insert mode
- `Esc`: Exit insert mode

<!-- pause-->

## Saving and Quitting

- `:w`: Save the file
- `:q`: Quit Vim
- `:wq`: Save and quit
- `:q!`: Quit without saving
- `:qa!`: Quit all open files without saving

```
a is for all
```

<!-- pause-->

## Deleting and Yanking

- `dd`: Delete a line
- `x` or `d`: Delete a character (like CUT)
- `yy`: Copy a line
- `y`: Yank (copy) a word in Visual Mode
- `p`: Paste

<!-- pause-->

## Cursor Movement

- `0`: Move to the beginning of a line
- `$`: Move to the end of a line
- `^`: Move to the first non-blank character of a line
- `b`: Move backward to the beginning of a word
- `e`: Move to the end of a word
- `f`: Find a character in the current line
- `g`: Go to (various commands)
- `h`: Move cursor left
- `j`: Move cursor down
- `k`: Move cursor up
- `l`: Move cursor right
- `%`: Move to the matching parenthesis

<!-- end_slide-->

## Editing Text

<!-- pause-->

- `A`: Append text at the end of a line
- `a`: Append text after the cursor
- `c`: Change (delete and enter insert mode)
- `C`: Change to the end of a line
- `d`: Delete text
- `o`: Open a new line below the current line
- `O`: Open a new line above the current line

<!-- pause-->

## Repeating and Searching

<!-- pause-->

- `n`: Repeat the last search

## Using Numbers

<!-- pause-->

- `2j`: Move cursor down 2 lines
- `3dd`: Delete 3 lines
- `4yy`: Copy 4 lines

## Moving around

<!-- pause-->

- `{`: Move to the beginning of a paragraph
- `}`: Move to the end of a paragraph

- `gg`: Move to the beginning of the file
- `G`: Move to the end of the file
- `H`: Move to the top of the screen
- `M`: Move to the middle of the screen
- `L`: Move to the bottom of the screen
- `zz`: Center the screen on the cursor

- `Ctrl-u`: Move half a page up
- `Ctrl-d`: Move half a page down
- `Ctrl-b`: Move a page up
- `Ctrl-f`: Move a page down

<!-- end_slide-->

## Structure of a Vim Command

<!-- pause-->

A Vim command typically consists of three parts:

1. **Range**: The scope of the command (e.g., `2` for two lines, `w` for a word).
2. **Command**: The action you want to perform (e.g., `d` for delete, `y` for yank).
3. **Motion**: The movement or target of the command (e.g., `j` for down, `w` for word).
<!-- pause-->

For example, in the command `3dd`:

- `3` is the range (three lines),
- `d` is the command (delete),
- `d` is the motion (lines).

This structure allows for powerful and flexible text manipulation in Vim.

<!-- pause-->

## More Examples

- `d2w`: Delete two words
- `d$`: Delete to the end of the line
- `d0`: Delete to the beginning of the line
- `ciw`: Change the inner word
- `caw`: Change a word
- `ci"`: Change the text inside quotes

<!-- end_slide-->

# Buffers

<!-- pause-->

Vim maintains a set of open files, called `buffers`.

- A Vim session has a number of tabs, each of which has a number of windows (split panes).
- Each window shows a single buffer. Unlike other programs you are familiar with, like web browsers, there is not a 1-to-1 correspondence between buffers and windows; windows are merely views.
- A given buffer may be open in multiple windows, even within the same tab. This can be quite handy, for example, to view two different parts of a file at the same time.

- Buffers are in-memory text files that you can edit.
- Use `:ls` to list all open buffers.
- Use `:b <buffer_number>` to switch to a specific buffer.
- Use `:bd <buffer_number>` to delete a buffer.

<!-- end_slide-->

# The ":" Command-line Inside Terminal

<!-- pause-->

- The `:` character is used to enter `command-line` mode in Vim.
- Commands entered after `:` are executed by Vim.
- Examples: `:w` to save, `:q` to quit, `:help` to open help.
<!-- pause-->

- If you want to see keymaps in normal, insert or visual mode, you can use `:map`, `:imap`, `:vmap`, etc.

- Use `/` to search for text in the file, and `n` to go to the next match.

## Additional Commands

- `u`: Undo the last change
- `Ctrl + r`: Redo the undone change
- `:set number`: Show line numbers
- `:set nonumber`: Hide line numbers
- `:syntax on`: Enable syntax highlighting
- `:syntax off`: Disable syntax highlighting

<!-- end_slide-->

# Registers

<!-- pause-->

Vim has a set of `registers` that can be used to store text. Registers can be used to store text that can be pasted later. Registers can be accessed using the `"` character followed by the register name.

- `""`: The unnamed register, which is the default register.
- `"0`: The yank register, which stores the last yanked text.
- `"1` to `"9`: The numbered registers, which store the last 9 deleted or changed text.
- `"+`: The system clipboard register, which can be used to copy text to the system clipboard.
- `"_`: The black hole register, which can be used to delete text without storing it in a register.

# Customizing Vim

- **.vimrc**: The configuration file for Vim
- **Plugins**: Extend Vim's functionality using plugins like Pathogen, Vundle, or Vim-Plug
- **Themes**: Customize the appearance of Vim using color schemes

<!-- pause-->

## NEOVIM

```
THE GOATED VIM
```

```
In My Opinions
```

<!-- end_slide-->

# More Cool Stuff you can do in Vim

## Search And Replace

## Macros

## Splitting Windows

## Full blown configured Neovim

<!-- end_slide-->

# Terminal Multiplexers

Terminal multiplexers allow you to manage multiple terminal sessions from a single window. They enable you to switch between different tasks without opening multiple terminal windows.

<!-- pause-->

# Inbuilt Multiplexers

Some terminal emulators come with built-in multiplexing capabilities. These allow you to split your terminal window into multiple panes and manage different tasks within the same window.

<!-- pause-->

Today almost all terminal emulators have this feature.
Example:-

- **Ghostty**
- **iTerm2**
- **Alacritty**
- **Kitty**
- **Wezterm**
- ETC.

<!-- end_slide-->

# TMUX

TMUX is a powerful terminal multiplexer that allows you to create, manage, and navigate between multiple terminal sessions within a single window. It is highly configurable and supports features like session persistence, window splitting, and more.

<!-- pause-->

## Why Use TMUX?

<!-- pause-->

- **SSH Sessions**: TMUX allows you to manage multiple SSH sessions from a single terminal window.
- **Productivity**: TMUX helps you stay organized by allowing you to manage multiple tasks efficiently.
- **Session Persistence**: TMUX allows you to detach from a session and reattach to it later.
- **Window Splitting**: TMUX supports both vertical and horizontal window splitting.
- **Customizability**: TMUX can be customized using configuration files.

<!-- end_slide-->

# Basic TMUX Commands

- `tmux new -s <session_name>`: Create a new TMUX session
- `tmux attach -t <session_name>`: Attach to an existing TMUX session
- `tmux detach`: Detach from the current TMUX session
- `tmux ls`: List all TMUX sessions
- `Ctrl-b %`: Split the current pane vertically
- `Ctrl-b "`: Split the current pane horizontally
- `Ctrl-b o`: Switch to the next pane
- `Ctrl-b x`: Close the current pane

<!-- pause-->

# Customizing TMUX

<!-- pause-->

- **.tmux.conf**: The configuration file for TMUX
- **Plugins**: Extend TMUX's functionality using plugins like Tmux Plugin Manager (TPM)
- **Themes**: Customize the appearance of TMUX using color schemes and themes

<!-- end_slide-->

# Conclusion

<!-- pause-->

Vim is a powerful text editor that can greatly enhance your productivity as a developer. With features like modal editing, customizability, and extensibility, Vim is a versatile tool that can be tailored to your needs.

<!-- pause-->

Terminal multiplexers like TMUX can greatly enhance your productivity by allowing you to manage multiple terminal sessions efficiently. With features like session persistence and window splitting, TMUX is a powerful tool for any developer.

<!-- pause-->

## ANY QUESTIONS?
