import random

def dig(tilemap,tile,x,y,decay = 0,max=20):
	ch = random.choice([1,2,3,4])
	while (max >= 0):
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