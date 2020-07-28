#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 
bt=[1,80,3,12,57,216,13,7,170,169]
#get player tilepos
pos=mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
for i in range(10):
    mc.setBlock(x+i,y,z,bt[i])
    time.sleep(2)
#setblock
'''bt=1
x=x+1
mc.setBlock(x,y,z,bt)
time.sleep(2)
mc.postToChat("setblock-stone")

bt2=80
x=x+1
mc.setBlock(x,y,z,bt2)
time.sleep(2)
mc.postToChat("setblock-snow")

bt3=3
x=x+1
mc.setBlock(x,y,z,bt3)
time.sleep(2)
mc.postToChat("setblock-dirt")

bt4=12
x=x+1
mc.setBlock(x,y,z,bt4)
time.sleep(2)
mc.postToChat("setblock-sand")

bt5=57
x=x+1
mc.setBlock(x,y,z,bt5)
time.sleep(2)
mc.postToChat("setblock-diamond block")

bt6=216
x=x+1
mc.setBlock(x,y,z,bt6)
time.sleep(2)
mc.postToChat("setblock-bone block")

bt7=13
x=x+1
mc.setBlock(x,y,z,bt7)
time.sleep(2)
mc.postToChat("setblock-gravel")

bt8=7
x=x+1
mc.setBlock(x,y,z,bt8)
time.sleep(2)
mc.postToChat("setblock-bedrock")
bt9=170
x=x+1
mc.setBlock(x,y,z,bt9)
time.sleep(2)
mc.postToChat("setblock-haybale")
#other block:in else
bt10=169
x=x+1
mc.setBlock(x,y,z,bt10)
time.sleep(2)
mc.postToChat("setblock-sea lantern")'''


#other
#bt = mc.getBlock(x,y,z)
print(bt)

for i  in range(10):
    bt = mc.getBlock(x-i,y,z)
    time.sleep(2)
    if(bt==1):
        mc.postToChat("stone")
    elif(bt==80):
        mc.postToChat("snow")
    elif(bt==3):
        mc.postToChat("dirt")
    elif(bt==12):
        mc.postToChat("sand")
    elif(bt==57):
         mc.postToChat("diamond block")
    elif(bt==216):
        mc.postToChat("bone block")
    elif(bt==13):
        mc.postToChat("gravel")
    elif(bt==7):
        mc.postTochat("bedrock")
    elif(bt==170):
        mc.postToChat("haybale")
    else:
        mc.postToChat("Information is not earned!")
