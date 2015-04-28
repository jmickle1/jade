from tilemap import *
import toolbox.draw
from brush import *
from tile import *
import thingplace
import random
from doomthings import *

def run():
	print("Running bronze_base.py")
	room_index = 0
	
	def room(tilemap,x,y,dir,room_index):
		
		width = random.randint(4,16)
		height = random.randint(4,16)
		offset = random.randint(0,5)
		rx = x
		ry = y
		if (dir == 0 or dir == 2): ry += offset
		if (dir == 1 or dir == 3): rx += offset
		if (dir == 1): ry -= height
		if (dir == 2): rx -= width
		
		def overlap(tilemap,x,y,w,h):
			for i in range(x,x+w):
				for j in range(y,y+h):
					if (tilemap.get_tile(i,j) != ""):
						return True
			return False
		
		timeout = 0
		while (overlap(tilemap,x,y,width,height)):
			width = random.randint(4,16)
			height = random.randint(4,16)
			offset = random.randint(0,5)
			rx = x
			ry = y
			if (dir == 0 or dir == 2): ry += offset
			if (dir == 1 or dir == 3): rx += offset
			if (dir == 1): ry -= height
			if (dir == 2): rx -= width
			timeout += 1
			if (timeout > 15):
				return
		
		#main room brush
		b = Brush("FLOOR7_1","SLIME14","BRONZE1",192)
		tilemap.set_tile_brush(str(room_index),Tile(0,128,b))
		toolbox.draw.rect(tilemap,str(room_index),x,y,width,height,1)
		#support detail brush
		d = Brush("FLAT5_4","FLAT5_4","SUPPORT3",192)
		tilemap.set_tile_brush(str(room_index)+"d",Tile(0,0,d))
		
		
		if (random.random() < 0.4):
			tilemap.set_tile(x,y,str(room_index)+"d")
			tilemap.set_tile(x + width-1,y,str(room_index)+"d")
			tilemap.set_tile(x,y+height-1,str(room_index)+"d")
			tilemap.set_tile(x+width-1,y+height-1,str(room_index)+"d")
		
		
		
		#exit
		new_dir = random.choice([dir+1,dir,dir+3])
		new_dir = new_dir%4
		room_index += 1
		if (room_index < 5):
			if (dir == 0): room(tilemap,x+width,y+height/2,new_dir,room_index)
			if (dir == 1): room(tilemap,x+width/2,y,new_dir,room_index)
			if (dir == 2): room(tilemap,x,y+height/2,new_dir,room_index)
			if (dir == 3): room(tilemap,x+width/2,y+height,new_dir,room_index)

	tilemap = Tilemap(100,100)
	room(tilemap,50,50,0,room_index)
	thingplace.place(tilemap,PLAYER1,96,96)
	print("Completed tilemap generation")
	return tilemap