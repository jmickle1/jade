import util
import omg
import omg.mapedit
import subprocess
import os
import sys

zdbsp_path = os.path.dirname(os.path.abspath(__file__)) + "/junk/zdbsp.exe"

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
		sss = tile_to_sector(tilemap,t)
		
		for s in sss:
			#convert to x,y tuples i guess
			newsect = []
			newsect.append((s[0][0],s[0][1]))
			#newsect.append((s[len(s)-1][0],s[len(s)-1][1]))
			for l in reversed(s):
				#n = (l[0],l[1])
				#newsect.append(n)
				n = (l[2],l[3])
				newsect.append(n)
			#newsect.append((s[len(s)-1][0],s[len(s)-1][1]))
			#newsect.append((s[0][0],s[0][1]))
			
			sec = tilemap.tileinfo[t].sector
			sid = tilemap.tileinfo[t].sidedef
			#print(newsect)
			map.draw_sector(newsect,sec,sid)
			sys.stdout.write(str(sss.index(s)+1)+"/"+str(len(sss))+" "+str(tilemap.tileindex.index(t)+1)+"/"+str(len(tilemap.tileindex))+"\r")
		
	sys.stdout.write("\n")
			
	
	## old drawing code ##
	#convert all tiles to square sectors
	# for i in range(tilemap.width):
		# for j in range(tilemap.height):
			# if (tilemap.get_tile(i,j) != ""):
				# sec = tilemap.tileinfo[tilemap.get_tile(i,j)].sector
				# sid = tilemap.tileinfo[tilemap.get_tile(i,j)].sidedef
				# map.draw_sector([(i*32,j*32),((i*32)+32,j*32),((i*32)+32,(j*32)+32),(i*32,(j*32)+32)],sec,sid)
		# sys.stdout.write(str(i+1)+"/"+str(tilemap.width)+"\r")
	# sys.stdout.write("\n")
				
				
	##--  this can only be implemented when overlapping lines are added in omgifol  --##	
	
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

def tile_to_sector(tilemap,tile):
	sectors = []
	#for each tile in a set, check the sides:
	#(left,top,right,bottom) all bools
	#True if that side doesn't connect to one the same
	#do this for all matching tiles
	#then check which ones connect to each other?
	#organize those into seperate distinct sectors
	#but draw with the same data
	lines = []
	#lines are just xy pairs (x1,y1,x2,y2)
	for i in range(0,tilemap.width):
		for j in range(0,tilemap.height):
			if (tilemap.get_tile(i,j) == tile):
				left = False
				up = False
				right = False
				down = False
				if (tilemap.get_tile(i+1,j) == tile): left = True
				if (tilemap.get_tile(i,j-1) == tile): up = True
				if (tilemap.get_tile(i-1,j) == tile): right = True
				if (tilemap.get_tile(i,j+1) == tile): down = True
				if (left == False): 
					lines.append([32+i*32,32+j*32,32+i*32,j*32])
				if (down == False): 
					lines.append([i*32,32+j*32,32+i*32,32+j*32])
				if (right == False): 
					lines.append([i*32,j*32,i*32,32+j*32])
				if (up == False): 
					lines.append([32+i*32,j*32,i*32,j*32])
				
	#loop through the lines and make connected sectors i guess?
	lines_checked = [False for c in range(len(lines))]
	def find_connects(line):
		#recursive function to mark lines connected to each other
		lines_checked[line] = True
		
		for l in range(0,len(lines)):
			if (lines_checked[l] == False):
				# if (lines[l][0] == lines[line][0] and lines[l][1] == lines[line][1]):
					# find_connects(l)
				# if (lines[l][2] == lines[line][2] and lines[l][3] == lines[line][3]):
					# find_connects(l)
				# if (lines[l][0] == lines[line][2] and lines[l][1] == lines[line][3]):
					# find_connects(l)
				if (lines[l][2] == lines[line][0] and lines[l][3] == lines[line][1]):
					find_connects(l)
		
		sectors[len(sectors)-1].append(lines[line]) #verified line
		
		
	#so until we have sorted all lines into sectors...
	while (False in lines_checked):
		sectors.append([])
		find_connects(lines_checked.index(False))
		
	return sectors
	
def to_file(tilemap,path):
	wad = omg.WAD()
	wad.maps["MAP01"] = to_map(tilemap)
	wad.to_file(path)
	print(path)
	print(zdbsp_path)
	subprocess.call([zdbsp_path,"-o"+path,path])
	print("zdbsp done!")
	
	
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