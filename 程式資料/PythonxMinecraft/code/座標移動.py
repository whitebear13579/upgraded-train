#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
import  time

pos = mc.player.getTilePos()
x1 = pos.x
y1=pos.y
z1=pos.z

time.sleep(5)

pos2=mc.player.getTilePos()
x2= pos2.x
y2= pos2.y
z2 = pos2.z

xm = x2-x1
ym = y2-y1
zm = z2-z1
bt=103
bt2=0

mc.setBlocks(x1,y1,z1,x2,y2,z2,bt)
mc.setBlocks(x1+2,y1+2,z1+2,x2+2,y2+2,z2+2,bt2)
mc.postToChat("huanghuamg moved x:"+str(xm) + ",y:" +  str(ym) +", and z: " + str(zm))
mc.postToChat("huanghuamg,the test is end!")


print("end test")
                                                                         
    
