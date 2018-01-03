from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

ids = mc.getPlayerEntityIds()

print (ids)

distances = []

for x in ids:
    pos = mc.entity.getPos(x)
    print (pos)
    distance = pos.x * pos.x + pos.y * pos.y + pos.z * pos.z
    print (distance)
    distances.append(distance)

print (distances)
