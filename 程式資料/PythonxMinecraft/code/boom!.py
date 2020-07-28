#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

k = "yes"
n = "no"
attmept = input("god:do you want some diamond?,say [yes]or[no]")
if attmept == k:
    p = mc.player.getTilePos()
    x = p.x
    y = p.y
    z = p.z
    bt = 57
    bt2 = 1
    mc.setBlocks(p.x,p.y-3,p.z-1,p.x+2,p.y-1,p.z+1,bt)
    mc.postToChat("magic")
elif attmept == n:

    print("ok,i m sorry i bother you.")

    time.sleep(1)

    print("app end")
    mc.postToChat("app end")
    
    
    

    


