#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

posi=mc.player.getTilePos()

x=posi.x
y=posi.y
z=posi.z

y=y+100

mc.player.setTilePos(x,y,z)

blocktype=1
blocktype2=46
blocktype3=152

y=y+1
mc.setBlock(x,y,z,blocktype)

y=y+1
mc.setBlock(x,y,z,blocktype2)

y=y+1
mc.setBlock(x,y,z,blocktype3)

print("end")


