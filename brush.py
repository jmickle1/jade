import omg.mapedit

class Brush(object):
	def __init__(self,floor = "SLIME14",ceil = "CEIL1_2",texture = "METAL2",z_floor = 0,z_ceil = 128,light=160):
		self.floor 	= floor
		self.ceil = ceil
		self.texture = texture
		self.z_floor = z_floor
		self.z_ceil = z_ceil
		self.light = light
		
	def to_sector(self):
		return omg.mapedit.Sector(self.z_floor,self.z_ceil,self.floor,self.ceil,self.light)