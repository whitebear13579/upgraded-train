#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#Set x, y, and z variables to represent coordinates
x = 196.294
y = 72.0
z =-65.679

#Change the player's position
mc.player.setPos(x,y,z)

#wait 8 second
time.sleep(8)

#Set x, y, and z variables to represent coordinates
x = 196.213
y = 95.75106
z = -53.126

#Change the player's position
mc.player.setPos(x,y,z)
