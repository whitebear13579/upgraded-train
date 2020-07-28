#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

p = mc.player.getTilePos()
x = p.x
y = p.y
z = p.z
#mc.setBlock(x,y,z,blocktype2)
blocktype = 95
y=y+1
mc.setBlock(x,y,z,blocktype)


for i in range(0,15):
    y=y+1
    mc.setBlock(x,y,z,blocktype,i)
print("end")
mc.postToChat(" THE TEST IS END!")


