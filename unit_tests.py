print("unit_tests.py")
from tilemap import *
from brush import *
from tile import *
import output
import omg.mapedit

tilemap = Tilemap(4,4)
tilemap.CLEANUP = True
b = Brush("SLIME14","FLOOR7_1","STONE4",176)
t = Tile(0,128,b)
tilemap.set_tile(1,1,t)
tilemap.set_tile(1,2,t)
tilemap.set_tile(2,1,t)
tilemap.set_tile(2,2,t)

map = output.to_map(tilemap)

me = omg.mapedit.MapEditor(map)
if (len(me.linedefs) != 4):
	print("Error: there are {0} linedefs and should be 4".format(len(me.linedefs)))
else:
	print("Test success")