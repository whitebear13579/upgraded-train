#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
import time

mc.postToChat("Surprise ")

time.sleep(5)

mc.postToChat("fuck")

print("end")

mc.postToChat(" THE TEST IS END!")

