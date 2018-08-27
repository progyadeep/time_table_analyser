from PIL import Image
import json
import numpy as np

###### PREPROC_BETA PROCESS
def dist(f, t):
	return int((abs(f[0]-t[0])**2 + abs(f[1]-t[1])**2 + abs(f[2]-t[2]))**0.5)

def preproc_beta(p):
	p=p[0:3]
	if p[0] <= 200 and p[1] <= 200 and p[2] <= 200: #preprocessing 1
		return (0,0,0)
	elif p[1] > 200 and p[2] > 200 and p[2] >= p[1]: #preprocessing 2
		return (0,0,200)
	else: #preprocessing 3 (monotonizing 2)
		dg = dist((203,254,51), p)
		dy = dist((255,255,204), p)
		if dg < dy:
			return (0,255,0)
		else:
			return (255,255,0)
####################
### GLOBALS ########

cd = [0,0]

def updateNPCoord():
    global cd
    if cd[1] < 12:
        cd = [cd[0], cd[1]+1]
    else:
        cd = [cd[0]+1, 0]

def slot(loc):
	global cd
	cd=[0,0]
	slot_state = np.zeros((14,13))
	hops = []
	final_list = []
	tt = Image.open(loc).rotate(180)
	dim = tt.size


	'''
	filled slot = (0,255,0)
	empty slot = (255,255,0)
	'''

	cols = [(0,255,0),(255,255,0)]

	start = [] ##coordinates of the starting point

	i=0
	while i < dim[0]:
		j = 0
		while j < dim[1]:
			rgb = preproc_beta(tt.getpixel((i,j)))
			if rgb == (255,255,0) or rgb == (0,255,0):
				start = [i,j]
				i = dim[0] #breaking the outer loop
				break #breaking the inner loop
			j = j + 1
		i = i + 1


	j = start[1]
	i = start[0]


	try:
		for b in range(14):

			for a in range(13):
				if preproc_beta(tt.getpixel((i,j))) == (0,255,0):
					slot_state[cd[0], cd[1]] = 1

				updateNPCoord()

				if a == 12:
					break
				
				if b == 0:
					h = 1
					i = i + 1
					while preproc_beta(tt.getpixel((i,j))) != (0,0,0):
						i = i + 1
						h = h + 1
					while preproc_beta(tt.getpixel((i,j))) not in cols:
						i = i + 1
						h = h + 1
					hops.append(h)
				else:
					i = i + hops[a]

			#printing
			#for x in range(13):
			#    print(int(slot_state[b][a]), end=' ')
			#print('\n')

			if b == 13:
				break


			i = start[0]
			j = j + 1
			while preproc_beta(tt.getpixel((i,j))) != (0,0,0):
				j = j + 1
			while preproc_beta(tt.getpixel((i,j))) not in cols:
				j = j + 1

	except IndexError:
		if cd[0] < 10 or cd[1] != 0:
			return
			# print("BAD FILE: Please upload a proper time table image.")
			# exit()

	##in case of a correctly cropped image, empty rows need be added to the top
	##of the table, before rotation
	for x in range(14 - cd[0]):
		tr = np.zeros(13)
		i = 13
		while i >= 1:
			slot_state[i] = slot_state[i-1]
			i = i - 1
		slot_state[0] = tr

	##rotating the array
	slot_state = np.rot90(slot_state, 2, (0,1))

	a = 0
	while a < 13:
		b = 0
		while b < 13:
			final_list.append(int(slot_state[a,b] + slot_state[a+1, b]))
			b = b + 1
		a = a + 2

	return final_list

loc=input('location ')
print(slot(loc))
# print(slots(loc))
# print(slots(loc))
