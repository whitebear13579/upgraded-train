#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
for i in range(30):
    p = mc.player.getPos()
    x = p.x
    y = p.y
    z = p.z
    bt = 46
    mc.setBlock(p.x,p.y-1,p.z,bt)
    time.sleep(1)
    print(i)
