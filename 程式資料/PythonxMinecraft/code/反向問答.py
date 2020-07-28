#Connect to Minecraft
def no(s,b,d,bone,block):
    if(block==s or block==b or block==d or block==bone):
        return True
    else:
        return False
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

p=mc.player.getTilePos()
x = p.x
y = p.y
z = p.z

#stone
s = 1
#bedrock
b = 7
#diamond block
d = 57
#bone block 
bone = 216

block = mc.getBlock(x,y-1,z)
#hi=no(s,b,d,bone,block)
hi=(block==s or block==b or block==d or block==bone)
print(hi)
if(not hi):    
    mc.postToChat("GOD:you need somthing!"+str(hi)  )
else:
     mc.postToChat("WOW")
print("end")


