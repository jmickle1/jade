import random
import toolbox.digger
from brush import *
from tile import *
import omg.mapedit
import thingplace
from doomthings import *
from tilemap import *

def run():

	tilemap = Tilemap(200,200)
	tilemap.CLEANUP = True
	corridor_brush = Brush("SLIME14","FLOOR7_1","STONE4",176)
	room_brush = Brush("FLOOR7_1","SLIME14","BRONZE1",192)
	corridor_tile = Tile(0,96,corridor_brush)
	room_tile = Tile(0,128,room_brush)
	
	
	def room(x,y):
		texture = random.choice(["METAL2","BRONZE1","STARTAN2"])
		floor = random.choice(["FLOOR7_1","SLIME14","FWATER1"])
		ceil = random.choice(["FLOOR7_1","SLIME14","F_SKY1"])
		z_floor = 0
		z_ceil = 128
		if (floor == "FWATER1"): z_floor -= 8
		if (ceil == "F_SKY1"): z_ceil += 32
		brush = Brush(floor,ceil,texture,192)
		tile = Tile(z_floor,z_ceil,brush)
		width = random.choice([6,7,8,9,10,12,16])
		height = random.choice([6,7,8,9,10,12,16])
		for a in range(x-width/2,x+width/2):
			for b in range(y-height/2,y+height/2):
				tilemap.set_tile(a,b,tile)
	
	def corridor_digger(x,y,chance,tile):
		width = random.choice([3,4,5])
		life = 30
		dir = random.choice([0,1,2,3])
		while (life > 0):
			life-=1
			for a in range(x-width/2,x+width/2):
				for b in range(y-width/2,y+width/2):
					tilemap.set_tile(a,b,tile)
			if (dir == 0): x += 1
			if (dir == 1): y -= 1
			if (dir == 2): x -= 1
			if (dir == 3): y += 1
			if (random.random() < 0.1):
				dir += random.choice([-1,1])
				dir %= 4
				if (random.random() < chance):
					chance *= 0.7
					corridor_digger(x,y,chance,tile)
				if (random.random() < 0.5):
					room(x,y)
		room(x,y)
	
	corridor_digger(100,100,1,corridor_tile)		
	
	return tilemap