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
	room_brush = Brush("FLOOR7_1","SLIME14","BRONZE1",192)
	room_tile = Tile(0,128,room_brush)
	
	tilemap.set_tile_brush("food",room_tile)
	
	def room(x,y):
		width = random.choice([6,7,8,9,10,12,16])
		height = random.choice([6,7,8,9,10,12,16])
		for a in range(x-width/2,x+width/2):
			for b in range(y-height/2,y+height/2):
				tilemap.set_tile(a,b,"food")
	
	def corridor_digger(x,y,chance):
		width = random.choice([3,4,5])
		life = 50
		dir = random.choice([0,1,2,3])
		while (life > 0):
			life-=1
			for a in range(x-width/2,x+width/2):
				for b in range(y-width/2,y+width/2):
					tilemap.set_tile(a,b,"food")
			if (dir == 0): x += 1
			if (dir == 1): y -= 1
			if (dir == 2): x -= 1
			if (dir == 3): y += 1
			if (random.random() < 0.05):
				dir += random.choice([-1,1])
				dir %= 4
				if (random.random() < chance):
					chance *= 0.6
					corridor_digger(x,y,chance)
				if (random.random() < 0.5):
					room(x,y)
		room(x,y)
	
	corridor_digger(100,100,1)		
	
	return tilemap