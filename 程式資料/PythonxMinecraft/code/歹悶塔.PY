#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
bt=57
s=0
mh=3
for fuck in  range( s,mh):
 mc.setBlocks(x+fuck,y-fuck+1,z-fuck,x-fuck,y-fuck+1,z+fuck,bt)


#x=x+1
#mc.setBlocks(x,y,z,x+w,y+h,z+l,bt)

#x = x+1
#y = y+1
#z = z+1
#mc.setBlocks(x,y,z,x+w-2,y+h,z+l-2,bt)

#x = x+1
#y = y+1
#z = z+1
#mc.setBlocks(x,y,z,x+w-4,y+h,z+4-4,bt)

#x = x
#y = y+1
#z = z
#mc.setBlocks(x,y,z,x+w-4,y+h,z+4-4,bt)

print("fuck! end")
