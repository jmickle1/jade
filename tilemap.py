class Tilemap(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = [["" for y in range(height)] for x in range(width)]
	
	def set_tile(self,x,y,tile):
		if (x >= 0 and y >= 0 and x < self.width and y < self.height):
			self.data[x][y] = tile
		else:
			print("tilemap.py trying to set out of bounds")
	
	def get_tile(self,x,y):
		if (x >= 0 and y >= 0 and x < self.width and y < self.height):
			return self.data[x][y]
		else:
			print("tilemap.py trying to read out of bounds")
		
	def get_size(self):
		return (self.width,self.height)