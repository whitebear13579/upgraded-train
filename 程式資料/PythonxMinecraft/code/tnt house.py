#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
posi=mc.player.getTilePos()
x =  posi.x
y = posi.y
z = posi.z

w=14
h=8
l=6
bt=42
w=9

mc.setBlocks(x,y,z,x+w,y+h,z+l,bt)
mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+l- 1,w)
print("end")
