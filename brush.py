import omg.mapedit

class Brush(object):
	def __init__(self,floor = "SLIME14",ceil = "CEIL1_2",texture = "METAL2",light=192):
		self.floor 	= floor
		self.ceil = ceil
		self.texture = texture
		self.light = light
		self.sidedef = omg.mapedit.Sidedef(0,0,"-","-",texture)