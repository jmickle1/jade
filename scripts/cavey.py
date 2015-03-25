import random
import toolbox.digger
import brush
import omg.mapedit
import thingplace
from doomthings import *
from tilemap import *

def run():
	tilemap = Tilemap(80,60)
	tilemap.set_tile_brush("A",brush.Brush(random_rock_flat(),random_rock_flat(),random_rock_texture(),random.choice([0,16,32,48]),random.choice([0,16,32,48])+96,random.choice([0,16,32,48])+128))
	tilemap.set_tile_brush("B",brush.Brush(random_rock_flat(),random_rock_flat(),random_rock_texture(),random.choice([0,16,32,48]),random.choice([0,16,32,48])+96,random.choice([0,16,32,48])+128))
	tilemap.set_tile_brush("C",brush.Brush(random_rock_flat(),random_rock_flat(),random_rock_texture(),random.choice([0,16,32,48]),random.choice([0,16,32,48])+96,random.choice([0,16,32,48])+128))
	tilemap.set_tile_brush("D",brush.Brush(random_rock_flat(),random_rock_flat(),random_rock_texture(),random.choice([0,16,32,48]),random.choice([0,16,32,48])+96,random.choice([0,16,32,48])+128))
	tilemap.set_tile_brush("E",brush.Brush(random_rock_flat(),random_rock_flat(),random_rock_texture(),random.choice([0,16,32,48]),random.choice([0,16,32,48])+96,random.choice([0,16,32,48])+128))
	toolbox.digger.dig(tilemap,"A",50,50,0,200,5)
	toolbox.digger.dig(tilemap,"B",50,50,0,200,5)
	toolbox.digger.dig(tilemap,"C",50,50,0,200,5)
	toolbox.digger.dig(tilemap,"D",50,50,0,200,5)
	toolbox.digger.dig(tilemap,"E",50,50,0,200,5)
	tilemap.things.append(omg.mapedit.Thing(50*32,50*32,0,PLAYER1))
	thingplace.add_to_tile_type(tilemap,"A",0.1,[ZOMBIEMAN,SHOTGUN_GUY,IMP,STIMPACK,AMMO_CLIP,SHELLS])
	thingplace.add_to_tile_type(tilemap,"B",0.1,[ZOMBIEMAN,SHOTGUN_GUY,IMP,STIMPACK,AMMO_CLIP,SHELLS])
	return tilemap
	
def random_rock_flat():
	return random.choice(["FLAT1_1"])
	#return random.choice(["MFLR8_2","MFLR8_3","MFLR8_4","FLAT1_1","FLAT1_2","FLAT5_7","FLAT5_8","GRNROCK","RROCK03","RROCK11","RROCK12","RROCK13"])

def random_rock_texture():
	return random.choice(["BRICK1"])
	#return random.choice(["ASHWALL2","ASHWALL3","ASHWALL4","ASHWALL6","ASHWALL7","BRICK1","BSTONE1","ROCK1","ROCK2","ROCK3","ROCK4","ROCK5","STONE4","STONE5","STONE6","STONE7"])