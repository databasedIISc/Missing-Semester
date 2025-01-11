# Vim Learning Playground

Welcome to the Vim Learning Playground! This file is your space to practice Vim commands, motions, and editing skills. Follow the instructions, play around with the text, and learn at your own pace.

## Random Piece of Code

Today we will make a special recipe for Pigs called "poo-pie"!

```python
def make_poo_pie(ingredients):
    pie = []
    for ingredient in ingredients:
        if ingredient == "poo":
            pie.append("poo")
        else:
            pie.append("not poo")
    return pie

def bake_poo_pie(pie):
    baked_pie = []
    for piece in pie:
        if piece == "poo":
            baked_pie.append("baked poo")
        else:
            baked_pie.append("baked not poo")
    return baked_pie

def decorate_poo_pie(baked_pie):
    decorated_pie = []
    for piece in baked_pie:
        if piece == "baked poo":
            decorated_pie.append("decorated baked poo")
        else:
            decorated_pie.append("decorated baked not poo")
    return decorated_pie

def serve_poo_pie(decorated_pie):
    for piece in decorated_pie:
        if piece == "decorated baked poo":
            print("Serving a piece of decorated baked poo")
        else:
            print("Serving a piece of decorated baked not poo")

ingredients = [
    "flour",
    "sugar",
    "poo",
    "eggs",
    "milk",
    "butter",
    "poo"
]
pie = make_poo_pie(ingredients)
baked_pie = bake_poo_pie(pie)
decorated_pie = decorate_poo_pie(baked_pie)
serve_poo_pie(decorated_pie)
```

## Random piece of ASCII Art

```
        1          _________________________
       11         |                         |
   111111         |   ALWAYS BE YOURSELF    |
 11_O-111         |   UNLESS YOU CAN BE A   |
1111111111        |   |  |   /\ |\/| /\     |
 11__11111      --|   |__|__/--\|  |/--\    |
 1___1111    --/  |_________________________|
 1___1111  -/
 1__1111
 1__1111
 1_11111       11111
 1_1111       1111111
 1_111111    111111111
 1__11111111111111111111
  1_111111111111111111111
   11111111111111111111111
     111111111111111111111
      1111111111111111111
      111111     1111111
       1111       111111
       111         11111
       111          111_1
       111          111_1
       111          11_1
       111          1111
      11           111
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

## Random piece of garbage

```c
#include <stdio.h>
#include <stdlib.h>

void do_nothing(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = array[i] * 2;
        array[i] = array[i] / 2;
    }
}

void print_random_numbers(int count) {
    for (int i = 0; i < count; i++) {
        printf("%d\n", rand() % 100);
    }
}

void reverse_array(int *array, int size) {
    for (int i = 0; i < size / 2; i++) {
        int temp = array[i];
        array[i] = array[size - i - 1];
        array[size - i - 1] = temp;
    }
}

void fill_with_zeros(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = 0;
    }
}

int main() {
    int array[10];
    for (int i = 0; i < 10; i++) {
        array[i] = i;
    }

    do_nothing(array, 10);
    print_random_numbers(5);
    reverse_array(array, 10);
    fill_with_zeros(array, 10);

    return 0;
}
```

## Random piece of shit

```

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠋⢩⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠐⠷⠤⠤⠤⠤⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠟⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠉⠀⠀⠀⠀⠈⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣀⡤⠤⠤⢄⡀⠀⠈⠙⠒⠦⣤⣀⣠⠖⠋⠉⠓⠦⣀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣿⣧⡞⠁⢀⣀⡀⠀⠙⣆⠀⠀⠀⠀⠀⡼⠁⠀⣠⣤⡀⠀⠙⡟⠿⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠟⠁⡼⠀⢠⣿⣿⣿⣦⠀⠘⡆⠀⠀⠀⢰⠇⠀⣼⣿⣿⣿⡄⠀⢹⠀⠀⠙⢿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡟⠀⠀⠀⡇⠀⢸⣿⣿⣿⣿⠆⠀⡧⠀⠀⠀⠸⡆⠀⣿⣿⣿⣿⡇⠀⢸⠇⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⠀⠀⠀⢻⡀⠘⣿⣿⣿⡿⠀⢀⠟⠦⢤⣀⡀⢳⠀⠘⢿⣿⠟⠀⠀⡼⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⢳⡀⠈⠉⠉⠀⢀⡞⠀⠀⠀⠈⠉⠙⠳⣄⠀⠀⠀⣠⣾⣁⣀⣀⣀⣠⣿⣤⣀⠀⠀⠀⠀
⠀⠀⠀⣀⣼⣿⡄⠀⠀⠀⠀⠙⠲⠤⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣦⠀⠀
⠀⣠⣾⠟⠉⠀⠙⢦⡀⠀⠀⠀⠀⣴⠒⠒⠲⠤⠤⠤⠴⠖⠒⠒⠒⠊⠉⢉⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⠀
⢰⡟⠁⠀⠀⠀⠀⠀⠉⠳⢤⣀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇
⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⡙⠲⠤⠤⣤⣤⠤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇
⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠲⠤⢤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀
⠀⠙⢷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣭⣽⣿⠶⠶⠶⣶⣤⣤⣤⣤⣤⣤⣤⣶⠿⠛⠀⠀
⠀⠀⠀⢉⣙⡛⠿⠷⠶⢶⣶⣶⣶⡶⠶⠶⠾⠿⠟⠛⠛⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀

```

## Random piece of Vim Memes link

- [vim-memes](https://github.com/kuator/Vim-memes)
- [r/ProgrammerHumor](https://www.reddit.com/r/ProgrammerHumor/comments/9lksci/vim_vs_emacs/), more [here](https://www.reddit.com/r/ProgrammerHumor/)
