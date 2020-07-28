#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

v = True

x = (int(input("E N T E R   Y O U R   X   P O I N T")))
y = (int(input("E N T E R   Y O U R   Y   P O I N T")))
z = (int(input("E N T E R   Y O U R   Z   P O I N T")))

if not(217<=x<=262):
        v = False
if not(100>=y>=68):
        v = False
if not(406>=z>=320):
        v = False
if v:
    mc.player.setTilePos
else:
    mc.postToChat("P L E A S E   P R E S S   A L L   P O I N T   A G A I N !")
    PRINT(
     
