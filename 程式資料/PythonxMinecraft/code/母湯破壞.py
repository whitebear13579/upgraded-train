#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

mc.setting("world_immutable",False)

mc.postToChat("block borken enable")

time.sleep(10)

mc.setting("world_immutable",True)

mc.postToChat("block borken disable")
time.sleep(10)
mc.setting("world_immutable",False)
mc.postToChat("block borken enable")




