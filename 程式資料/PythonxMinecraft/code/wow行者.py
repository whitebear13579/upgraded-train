#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
import random

bt=95
while True:
    p =mc.player.getTilePos()
    x = p.x
    y = p.y
    z = p.z
    i = random.randrange(0,15)
    
    mc.setBlock(p.x,p.y-1,p.z,bt,i)

