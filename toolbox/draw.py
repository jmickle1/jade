import util

def rect(tilemap,tile,x,y,w,h,fill = 0):
	if (fill == 0):
		for i in range(x,x+w):
			tilemap.set_tile(i,y,tile)
			tilemap.set_tile(i,y+h-1,tile)
		for j in range(y,y+h):
			tilemap.set_tile(x,j,tile)
			tilemap.set_tile(x+w-1,j,tile)
	else:
		for i in range(x,x+w):
			for j in range(y,y+h):
				tilemap.set_tile(i,j,tile)

def circle(tilemap,tile,x,y,radius):
	for i in range(x-radius,x+radius):
		for j in range(y-radius,y+radius):
			if (util.dist(i,j,x,y)<radius):
				tilemap.set_tile(i,j,tile)