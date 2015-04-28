import util
import omg
import omg.mapedit
import subprocess
import os
import sys

zdbsp_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/zdbsp.exe"
zennode_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/ZenNode.exe"

def to_image(tilemap):
	data = tilemap.data
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			print("output.to_image() not implemented")

def to_map(tilemap):
	
	sectors = []
	map = omg.mapedit.MapEditor()
	#print("drawing sectors")
	#draw all types of tile to seperate sectors
	for t in tilemap.tileindex:
		sss = tilemap.tile_to_sectors(t)
		
		for s in sss:
			newsect = []
			newsect.append((s[0][0],s[0][1]))
			for l in reversed(s):
				n = (l[2],l[3])
				newsect.append(n)
			
			sec = tilemap.tileinfo[t].sector
			sid = tilemap.tileinfo[t].brush.sidedef
			
			map.draw_sector(newsect,sec,sid)
			sys.stdout.write(str(sss.index(s)+1)+"/"+str(len(sss))+" "+str(tilemap.tileindex.index(t)+1)+"/"+str(len(tilemap.tileindex))+"\r")
		
	sys.stdout.write("\n")
	
	print("cleaning up sectors")
	
	for s1 in map.sectors:
		comb_list = []
		for s2 in map.sectors:
			if (s1 != s2):
				if (map.compare_sectors(s1,s2)):
					if (s2 not in comb_list):
						comb_list.append(s2)
		for c in comb_list:
			map.combine_sectors(s1,c)
		sys.stdout.write(str(map.sectors.index(s1)+1)+"/"+str(len(map.sectors))+"\r")
	sys.stdout.write("\n")
	
	#add things
	map.things = tilemap.things
	
	return map.to_lumps()
	
def to_file(tilemap,path,node_builder = "ZDBSP"):
	wad = omg.WAD()
	wad.maps["MAP01"] = to_map(tilemap)
	wad.to_file(path)
	if (node_builder == "ZDBSP"):
		subprocess.call([zdbsp_path,"-o"+path,path])
		print("zdbsp done!")
	if (node_builder == "ZENNODE"):
		subprocess.call([zennode_path,path])
		print("ZenNode done!")
	
	
	
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