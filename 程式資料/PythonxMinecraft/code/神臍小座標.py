#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
import  random

x = pos.x
y = pos.y
z = pos.z

x = x+random.randrange(-87,87)
y = y+random.randrange(0,256)
z = z+random.randrange(-87,87)
mc.player.setPos(x,y,z
print("end")
