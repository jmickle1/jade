import util
try:
	import omg
except:
	pass

def to_image(tilemap):
	data = tilemap.data
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			print("output.to_image() not implemented")

def to_map(tilemap):
	print("output.to_map() not implemented")
	#convert all tiles to square sectors
	sectors = []
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			if (tilemap.get_tile(i,j) != ""):
				sectors.append(util.Sect([(i,j),(i+32,j),(i+32,j+32),(i,j+32)]
				
	map = omg.mapedit.MapEditor()
	
	for s in sectors:
		map.draw_sector(s)
	
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