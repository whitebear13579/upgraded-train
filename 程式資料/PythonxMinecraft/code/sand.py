#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Set x, y, and z variables to represent coordinates
x = 214.87
y = 69.78
z = -64.243
#Change the player's position
mc.player.setPos(x,y,z)
