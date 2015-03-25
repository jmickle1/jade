import brush
import omg.util

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
	
	def set_tile_brush(self,tile,brush):
		self.tileindex.append(tile)
		self.tileinfo[tile] = brush
		
	def paste_tilemap(self, til, offset, paste_blanks = False):
		for i in range(0,len(til.width)):
			for j in range(0,len(til.height)):
				if (til.get_tile(i,j) == ""):
					if (paste_blanks):
						self.set_tile(i,j,tile.get_tile(i,j))
				else:
					self.set_tile(i,j,tile.get_tile(i,j))