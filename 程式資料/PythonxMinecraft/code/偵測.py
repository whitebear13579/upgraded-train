#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

#get player tilepos
pos=mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

#setblock
bt=1
x=x+1
mc.setBlock(x,y,z,bt)
mc.postToChat("setblock-stone")
time.sleep(1)

bt2=80
x=x+1
mc.setBlock(x,y,z,bt2)
mc.postToChat("setblock-snow")
time.sleep(1)

bt3=3
x=x+1
mc.setBlock(x,y,z,bt3)
mc.postToChat("setblock-dirt")
time.sleep(1)

bt4=12
x=x+1
mc.setBlock(x,y,z,bt4)
mc.postToChat("setblock-sand")
time.sleep(1)

bt5=57
x=x+1
mc.setBlock(x,y,z,bt5)
mc.postToChat("setblock-diamond block")
time.sleep(1)

bt6=216
x=x+1
mc.setBlock(x,y,z,bt6)
mc.postToChat("setblock-bone block")
time.sleep(1)

bt7=13
x=x+1
mc.setBlock(x,y,z,bt7)
mc.postToChat("setblock-gravel")
time.sleep(1)

bt8=7
x=x+1
mc.setBlock(x,y,z,bt8)
mc.postToChat("setblock-bedrock")
time.sleep(1)

bt9=170
x=x+1
mc.setBlock(x,y,z,bt9)
mc.postToChat("setblock-haybale")
time.sleep(1)

#other block:in else
bt10=169
x=x+1
mc.setBlock(x,y,z,bt10)
mc.postToChat("setblock-sea lantern")
time.sleep(1)

bt11 = 89
x = x+1
mc.setBlock(x,y,z,bt11)
mc.postToChat("setblock-glowstone")
time.sleep(1)

bt12 = 103
x = x+1
mc.setBlock(x,y,z,bt12)
mc.postToChat("setblock-watermelon")
time.sleep(1)

bt13 = 82
x = x+1
mc.setBlock(x,y,z,bt13)
mc.postToChat("setblock-clay")
time.sleep(1)


#other
bt = mc.getBlock(x,y-1,z)
print(bt)

p = mc.player.getTilePos()
x = p.x
y = p.y
z = p.z
mc.setBlock

for i  in range(13):
#在迴圈中偵測角下方塊
    p = mc.player.getPos()
    x = p.x
    y = p.y
    z = p.z
    bt=mc.getBlock(p.x,p.y-1,p.z)
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
        mc.postToChat("bedrock")
    elif(bt==170):
        mc.postToChat("haybale")
    else:
        mc.postToChat("Information is not earned!")
   #等待一秒
    time.sleep(1)
    #往前移動一格
    #p = mc.player.getTilePos()
    #x = p.x
    #y = p.y
    #z = p.z
    mc.player.setPos(p.x+1,p.y,p.z)
    pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
bt=57
bt2 = 0
s=0
mh=10
for fuck in  range( s,mh):
 mc.setBlocks(x+fuck+10,y-fuck+11,z-fuck,x-fuck+10,y-fuck+8,z+fuck,bt)
 mc.setBlocks(x+fuck+9,y-fuck+10,z-fuck+1,x-fuck+9,y-fuck+9,z+fuck-1,bt2)

 time.sleep(3)

x = pos.x
y = pos.y
z = pos.z
bt=51
s=0
mh=3
for fuck in  range( s,mh):
 mc.setBlocks(x+fuck+10,y-fuck+15,z-fuck,x-fuck+10,y-fuck+12,z+fuck,bt)
 
print("end---1")
mc.postToChat("thank for watching!")
mc.postToChat("and plz sub whitebear")
mc.postToChat("youtube search whiebear (chinese)")
mc.postToChat("After the program is executed, the self-destruct mode is enabled")

while True:
    p = mc.player.getTilePos()
    x = p.x
    y = p.y
    z = p.z
    bt = 46
    bt2 = 152
    mc.setBlock(p.x,p.y-1,p.z,bt)
    mc.setBlock(p.x,p.y-2,p.z,bt2)
    print("end---2")
    mc.postToChat("The program has been completely executed")
    mc.postToChat("T   H   E      E    N   D")
    


 
 


    


