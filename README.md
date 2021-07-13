# pyxel_examples

## Misc notes

https://www.lexaloffle.com/pico-8.php

https://tic80.com/

'z' and 'x' are common buttons in pico8 and tic80 games (like the a and b buttons on a gameboy)

`pyxel.blt()` https://en.wikipedia.org/wiki/Bit_blit

Press ALT+1 (OPT+1) during execution: Take a screenshot

Press ALT+3 (OPT+3) during execution: Save the last 30 seconds as an animated GIF

Press ALT+2 (OPT+2) during execution: Reset starting point of animated GIF

Each file is saved on your desktop

[Slides by the author of pyxel](https://docs.google.com/presentation/d/1fZomYz2kZtSpVeqXWfnHu1vUwzNEJ6McO83R58ePg3U/edit#slide=id.g90b0965fd1_0_4)

## Set up instructions

Here are some instructions to help you get Python, VSCode and Pyxel working on a non-school computer. Let me know if you can't get it all working.

### (Step 1) Install the latest versions of Python, VSCode and Git

Get the installers from the following links (make sure you choose the 64 bit Windows versions):

https://www.python.org/downloads/

https://code.visualstudio.com/download

https://git-scm.com/download/win

Run the three installers and follow their instructions.

*Important*: For the Python installer, just make sure you choose the option to 'add Python to PATH'. This should help VSCode find where you installed Python.

During the git installation, choose the option "Use VSCode as git's default editor".

### (Step 2) Download this repository

Open VSCode. Then choose 'Clone Repository', and paste in the url `https://github.com/mrmleonard/pyxel_examples`.

Open the file `pyxel/examples/00_hello_world.py`. VSCode should notice it's a `.py` python file and recommend you install the Python extension. One that is installed, you should see a green run button. Pressing that should run the program, which will open the terminal and print the message `Hello World!`.

Before we go on to step 2 (installed pyxel), let's learn how to use the terminal.

You can open the terminal in VSCode by going to `View>Terminal` in the top menu bar.

In the terminal, type `python` (if that doesn't work, try `python3` instead). This will open the python REPL shell inside of the terminal. You can type python code such as `1+2+3`.
To exit, type `exit()`. This will exit python and return you to the terminal.

You can also type `python pyxel/examples/00_hello_world.py` and press enter. This will run your main.py program through the python interpreter. Who needs a green run button when you have the terminal.

Now on to step 2...

### (Step 2) Install Pyxel

Pyxel is just a regular python package. You have all written 'import random' before to load the 'randint' function. 'random' is a python package that comes pre-installed when you install python. Similarly 'pyxel' is a python package - it just needs to be installed first before you can import it.

In the terminal type:

`pip install pyxel`

This should install pyxel. `pip` is short for 'package installer for python'. Suprise suprise: it installs packages. It is installed automatically when you install python, so you should already have the `pip` program.

### (Step 3) Run Pyxel

You should now be able to run any of the examples in the `examples` folder. Open an example file in VSCode and hit the green run button in the top right.

You can also run the editor by opening the file `pyxel/editor/__init__.py` and hitting the green run button in VSCode.

I've also included some existing games for you try in the `user_examples` folder.





