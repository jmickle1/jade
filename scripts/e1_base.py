from tilemap import *
import toolbox.draw
import brush
import tile
import thingplace
from doomthings import *

def run():
	tilemap = Tilemap(40,30)
	b = brush.Brush("FLAT5_4","CEIL3_5","STARG1",192)
	tilemap.set_tile_brush(".",tile.Tile(0,128,b))
	toolbox.draw.rect(tilemap,".",2,2,8,6,1)
	thingplace.place(tilemap,PLAYER1,96,96)
	return tilemap