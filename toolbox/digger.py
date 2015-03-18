import random
import math

def dig(tilemap,tile,x,y,decay = 0,max=20,thick=1):
	ch = random.choice([1,2,3,4])
	while (max >= 0):
		if (thick!=1):
			for a in range(int(x-thick/2),int(x+thick/2)):
				for b in range(int(y-thick/2),int(y+thick/2)):
					tilemap.set_tile(a,b,tile)
		else:
			tilemap.set_tile(x,y,tile)
		if (random.random()<0.5): 
			ch += random.choice([1,-1])
			if (ch>4): ch=0
			if (ch<0): ch=4
		if (ch==1): x+=1
		if (ch==2): y-=1
		if (ch==3): x-=1
		if (ch==4): y+=1
		if (random.random() < decay):
			max = 0
		max-=1