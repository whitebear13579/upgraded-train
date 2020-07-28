#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
attri={}
pos=mc.player.getPos()

stone = 1
grass = 2
attri["stone"]=1
attri["grass"]=2
attri["bedrock"]=7
#attri["1"]=1
for i in range(1,100):
    t=str(i)
    attri[t]=i

try:
    bt = str(input("PLEASE PRESS BLOCKNAME OR BLOCKTYPE\n"))

    mc.setBlock(pos.x,pos.y-1,pos.z,int(attri[bt]))

except:
    print("Your block name is not earned! Try to hit the block number or check the spelling!")

print("end") 

mc.postToChat("end")
