import brush
import omg.util
import math

class Tilemap(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = [["" for y in range(height)] for x in range(width)]
		self.tileinfo = omg.util.OrderedDict()
		self.tileindex = []
		self.things = []
	
	def set_tile(self,x,y,tile):
		try:
			self.tileinfo[tile]
		except:
			print("Tile "+tile+" has no Brush, creating default")
			self.set_tile_brush(tile,brush.Brush())
		if (x >= 0 and y >= 0 and x < self.width and y < self.height):
			self.data[x][y] = tile
	
	def get_tile(self,x,y):
		if (x >= 0 and y >= 0 and x < self.width and y < self.height):
			return self.data[x][y]
		else:
			return ""
		
	def get_size(self):
		return (self.width,self.height)
	
	def set_tile_brush(self,name,tile):
		self.tileindex.append(name)
		self.tileinfo[name] = tile
		
	def paste_tilemap(self, til, offset, paste_blanks = False):
		for i in range(0,len(til.width)):
			for j in range(0,len(til.height)):
				if (til.get_tile(i,j) == ""):
					if (paste_blanks):
						self.set_tile(i,j,tile.get_tile(i,j))
				else:
					self.set_tile(i,j,tile.get_tile(i,j))
					
	def tile_to_sectors(self,name):
		sectors = []
		lines = []
		#lines are just xy pairs (x1,y1,x2,y2)
		for i in range(0,self.width):
			for j in range(0,self.height):
				if (self.get_tile(i,j) == name):
					left = False
					up = False
					right = False
					down = False
					if (self.get_tile(i+1,j) == name): left = True
					if (self.get_tile(i,j-1) == name): up = True
					if (self.get_tile(i-1,j) == name): right = True
					if (self.get_tile(i,j+1) == name): down = True
					if (left == False): 
						lines.append([32+i*32,32+j*32,32+i*32,j*32])
					if (down == False): 
						lines.append([i*32,32+j*32,32+i*32,32+j*32])
					if (right == False): 
						lines.append([i*32,j*32,i*32,32+j*32])
					if (up == False): 
						lines.append([32+i*32,j*32,i*32,j*32])
					
		lines_checked = [False for c in range(len(lines))]
		def find_connects(line):
			#recursive function to mark lines connected to each other
			lines_checked[line] = True
			
			for l in range(0,len(lines)):
				if (lines_checked[l] == False):
					if (lines[l][2] == lines[line][0] and lines[l][3] == lines[line][1]):
						find_connects(l)
			
			sectors[len(sectors)-1].append(lines[line]) #verified line
			
		while (False in lines_checked):
			sectors.append([])
			find_connects(lines_checked.index(False))
			
		#return cleanup_lines(sectors)
		return sectors
		
def cleanup_lines(sectors):
	
	def line_compare(l1,l2):
		a1 = math.atan2(l1[3]-l1[1],l1[2]-l1[0])
		a2 = math.atan2(l2[3]-l2[1],l2[2]-l2[0])
		if (a1 == a2):
			return True
		return False
	
	output = []
	
	for s in sectors:
		new_sector = []
		i = 0
		new_line = [s[0][0],s[0][1],0,0]
		while (i < len(s)-1):
			if (line_compare(s[i],s[i+1])):
				i+=1
			else:
				new_line[2] = s[i][2]
				new_line[3] = s[i][3]
				new_sector.append(new_line)
				i+=1
				new_line = [s[i][0],s[i][1],0,0]
		new_sector.append(s[len(s)-1])
		output.append(new_sector)
	
	return output
	
