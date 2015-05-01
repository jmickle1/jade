import util
import omg
import omg.mapedit
import subprocess
import os
import sys

#define nodebuilder paths
zdbsp_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/zdbsp.exe"
zennode_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/ZenNode.exe"

def to_image(tilemap):
	'''Exports the tilemap to an image. Not implemented.
	Keeping it here so I make it eventually.
	'''
	data = tilemap.data
	for i in range(tilemap.width):
		for j in range(tilemap.height):
			print("output.to_image() not implemented")

def to_map(tilemap):
	'''Converts the tilemap to map data, ready to write to a WAD'''
	
	#Initialize map object
	map = omg.mapedit.MapEditor()
	
	#Initialize list of sectors
	sectors = []
	
	#draw all tiles to sectors
	for t in range(0,len(tilemap.tileindex)):
		
		#get current tile's sector conversion
		#each tile may have more than one sector, in the case of splits
		sss = tilemap.tile_to_sectors(t)
		
		#for each sector
		for s in sss:
			
			#build a list of vertices to draw the sector with
			newsect = []
			newsect.append((s[0][0],s[0][1]))
			for l in reversed(s):
				n = (l[2],l[3])
				newsect.append(n)
			
			#get the sector information from the tile
			sec = tilemap.tileindex[t].sector
			
			#get the sidedef information from the brush
			sid = tilemap.tileindex[t].brush.sidedef
			
			#draw the sector to the map
			map.draw_sector(newsect,sec,sid)
			
			#progress indicator
			sys.stdout.write(str(sss.index(s)+1)+"/"+str(len(sss))+" "+str(t+1)+"/"+str(len(tilemap.tileindex))+"  \r")
		
	sys.stdout.write("\n")
	
	print("cleaning up sectors")
	
	#combine all equivalent sectors
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
	'''Writes a tilemap straight to a .wad file
	
	Takes a nodebuilder selection for the third argument:
	"ZDBSP" for zdbsp
	"ZENNODE" for ZenNode
	'''
	
	#opens a new wad for writing
	wad = omg.WAD()
	
	#writes the map data to the MAP01 slot
	wad.maps["MAP01"] = to_map(tilemap)
	
	#saves the file
	wad.to_file(path)
	
	#runs the nodebuilder on the newly written file
	if (node_builder == "ZDBSP"):
		subprocess.call([zdbsp_path,"-o"+path,path])
		print("zdbsp done!")
	if (node_builder == "ZENNODE"):
		subprocess.call([zennode_path,path])
		print("ZenNode done!")
	
	
def to_print(tilemap):
	'''Prints a drawing of the tilemap to the console.
	
	Currently broken :~)
	'''
	print("printing tilemap")
	for j in range(tilemap.height):
		ln = ""
		for i in range(tilemap.width):
			if (tilemap.get_tile(i,j) != ""):
				ln += tilemap.get_tile(i,j)[0]
			else:
				ln += " "
		print(ln)