#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

bt = mc.getBlock(x,y-1,z)

inworld = bt ==2 or bt == 3 or bt == 1 or bt == 31
mc.postToChat( "the player are in the world?" + str(inworld))

