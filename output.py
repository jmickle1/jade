import util
import omg
import omg.mapedit
import subprocess
import os

zdbsp_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/zdbsp.exe"

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
				sec = tilemap.tileinfo[tilemap.get_tile(i,j)].sector
				sid = tilemap.tileinfo[tilemap.get_tile(i,j)].sidedef
				map.draw_sector([(i*32,j*32),((i*32)+32,j*32),((i*32)+32,(j*32)+32),(i*32,(j*32)+32)],sec,sid)
				
	print("output.py to_map(), cleaning up sectors")
	
	for s1 in map.sectors:
		comb_list = []
		for s2 in map.sectors:
			if (s1 != s2):
				if (map.compare_sectors(s1,s2)):
					if (s2 not in comb_list):
						comb_list.append(s2)
		for c in comb_list:
			map.combine_sectors(s1,c)
		#print(str(map.sectors.index(s1))+"/"+str(len(map.sectors)))
	
	return map.to_lumps()
	
def to_file(tilemap,path):
	wad = omg.WAD()
	wad.maps["MAP01"] = to_map(tilemap)
	wad.to_file(path)
	print(zdbsp_path)
	subprocess.call([zdbsp_path,"-o"+path,path])
	
	
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