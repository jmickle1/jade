import random
import toolbox.draw
import toolbox.digger

def run(tilemap):
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.draw.circle(tilemap,".",random.randint(0,30),random.randint(0,20),random.randint(3,8))
	toolbox.digger.dig(tilemap,"+",random.randint(0,30),random.randint(0,20))
	toolbox.digger.dig(tilemap,"+",random.randint(0,30),random.randint(0,20))
	x = random.randint(0,15)
	y = random.randint(0,10)
	w = random.randint(5,15)
	h = random.randint(4,10)
	toolbox.draw.rect(tilemap,"#",x,y,w,h,1)
	#toolbox.draw.rect(tilemap,"",x-1,y-1,w+2,h+2,0)