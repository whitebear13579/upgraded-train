#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

posi=mc.player.getTilePos()
x = posi.x
y = posi.y
z = posi.z

mc.player.setTilePos(x,y,z)

bt=109

z=z+1
mc.setBlock(x,y,z,bt)

y=y+1
z=z-2
mc.setBlock(x,y,z,bt)

y=y+1
z=z-2
mc.setBlock(x,y,z,bt)

z=z-1
mc.setBlock(x,y,z,bt)

