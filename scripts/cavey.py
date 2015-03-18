import random
import toolbox.digger
import brush

def run(tilemap):
	tilemap.set_tile_brush("+",brush.Brush("SLIME14","SLIME14","METAL2",0,96))
	tilemap.set_tile_brush("#",brush.Brush("SLIME14","F_SKY1","METAL2",16,128))
	tilemap.set_tile_brush("]",brush.Brush("SLIME14","SLIME14","METAL2",32,96))
	toolbox.digger.dig(tilemap,"+",30,15,0,30,2)
	toolbox.digger.dig(tilemap,"#",30,15,0,30,2)
	toolbox.digger.dig(tilemap,"]",30,15,0,30,2)