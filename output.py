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
	print("output.py to_map(), drawing sectors")
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			if (tilemap.get_tile(i,j) != ""):
				sec = tilemap.tileinfo[tilemap.get_tile(i,j)].to_sector()
				map.draw_sector([(i*32,j*32),((i*32)+32,j*32),((i*32)+32,(j*32)+32),(i*32,(j*32)+32)],sec)
				
	print("output.py to_map(), cleaning up sectors")
	combined = 0
	for s1 in map.sectors:
		comb_list = []
		for s2 in map.sectors:
			if (s1 != s2):
				if (map.compare_sectors(s1,s2)):
					if (s2 not in comb_list):
						combined+=1
						comb_list.append(s2)
		for c in comb_list:
			map.combine_sectors(s1,c)
			
	print("combined sectors: "+str(combined))
	
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