import omg.mapedit
import random

def add_to_tile_type(tilemap,tile,chance,things,angle=-1):
	if (angle == -1):
		angle = random.choice([0,90,180,270])
	for i in range(0,tilemap.width):
		for j in range(0,tilemap.height):
			if (tilemap.get_tile(i,j) == tile):
				if (random.random()<chance):
					thing = omg.mapedit.Thing(16+i*32,16+j*32,angle,random.choice(things))
					thing.easy = True
					thing.medium = True
					thing.hard = True
					tilemap.things.append(thing)