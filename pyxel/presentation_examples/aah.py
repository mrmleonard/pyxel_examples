import pyxel
import math

a=0
pyxel.init(128,128)
while 1:
 pyxel.cls(1)
 for x in range(0,128,4):
  for y in range(0,128,4):
   d=math.sqrt((x-64)**2+(y-64)**2)
   b=math.sin(d*0.2+a)*4
   c=(15-d*0.2)%16
   pyxel.circ(x+b,y+math.sin(b/4)*4,1,c)
 a+=0.2
 pyxel.flip()
