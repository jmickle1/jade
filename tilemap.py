import brush
import omg.util

class Tilemap(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = [["" for y in range(height)] for x in range(width)]
		self.tileinfo = omg.util.OrderedDict()
	
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
		
	def get_size(self):
		return (self.width,self.height)
	
	def set_tile_brush(self,tile,brush):
		self.tileinfo[tile] = brush