
# import Pyxel module
import pyxel

# set variables for animation
x = 0
# initialize the window with the init(width, height) command
pyxel.init(160, 120)

# game loop
while True:
    # update variables and call any drawing commands
    x += 2
    if x >= pyxel.width + 20:
        x = -20

    pyxel.cls(0)
    pyxel.circ(x=x, y=60, r=20, col=11)

    # update the screen with the flip command
    pyxel.flip()
