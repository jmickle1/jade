import random
import toolbox.draw
import toolbox.digger
import brush
import tile
from tilemap import *

def run():
	tilemap = Tilemap(10,10)
	b = brush.Brush("FLAT1_1","FLAT1_1","BRICK1",224)
	tilemap.set_tile_brush("A",tile.Tile(0,128,b))
	tilemap.set_tile_brush("B",tile.Tile(16,128,b))
	toolbox.draw.rect(tilemap,"A",0,0,2,2,1)
	toolbox.draw.rect(tilemap,"B",2,1,2,2,1)
	return tilemap