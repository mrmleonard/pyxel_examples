import pyxel

t=0
w=256
pyxel.init(w,w)
b=pyxel.image(0)
s=pyxel.image(4,system=True)
while 1:
    t += 1
    b.copy(0,0,4,0,0,w,w)
    s.copy(0,1,0,0,0,w,w)

    for x in range(w):
        if abs(t+((x-t)^(x+t))**3)%997<97:
            col = 7
        else: 
            col = 0
        pyxel.pset(x, 0, col)

    pyxel.flip()
