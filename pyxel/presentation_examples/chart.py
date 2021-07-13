# https://tkitao.hatenablog.com/entry/2019/09/22/001541

import pyxel

data = [40, 70, 50, 20, 100, 50, 40, 20]

pyxel.init(128, 128)

for i in range(len(data)):
    h = data[i]
    pyxel.rect(x = i * 14 + 10, y = 120 - h, w = 10, h = h, col = 8 + i)

pyxel.line(0, 120, 127, 120, 7)

pyxel.show()
