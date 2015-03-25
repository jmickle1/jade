import random
import toolbox.draw
import toolbox.digger
import brush

def run(tilemap):
	tilemap.set_tile_brush(".",brush.Brush("FWATER1","F_SKY1","STONE6",-8))
	toolbox.draw.rect(tilemap,".",0,0,1,1,1)