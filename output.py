import util
import omg
import omg.mapedit

def to_image(tilemap):
	data = tilemap.data
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			print("output.to_image() not implemented")

def to_map(tilemap):
	#convert all tiles to square sectors
	sectors = []
	map = omg.mapedit.MapEditor()
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			if (tilemap.get_tile(i,j) != ""):
				sec = tilemap.tileinfo[tilemap.get_tile(i,j)].to_sector()
				map.draw_sector([(i*32,j*32),((i*32)+32,j*32),((i*32)+32,(j*32)+32),(i*32,(j*32)+32)],sec)
	
	return map.to_lumps()
	
def to_print(tilemap):
	print("printing tilemap")
	for j in range(tilemap.height):
		ln = ""
		for i in range(tilemap.width):
			if (tilemap.get_tile(i,j) != ""):
				ln += tilemap.get_tile(i,j)[0]
			else:
				ln += " "
		print(ln)