#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

posi=mc.player.getTilePos()

x = posi.x
y = posi.y
z = posi.z

mc.player.setTilePos(x,y,z)

bt=10
bt2=152

y=y+2
mc.setBlock(x,y,z,bt)

time.sleep(1)

x=x+10
mc.player.setPos(x,y,z)

print("fuckkkkk")

