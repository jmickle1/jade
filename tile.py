import omg.mapedit

class Tile(object):
	def __init__(self,z_floor,z_ceil,brush):
		self.brush = brush
		self.z_floor = z_floor
		self.z_ceil = z_ceil
		self.sector = omg.mapedit.Sector(self.z_floor,self.z_ceil,brush.floor,brush.ceil,brush.light)