from PIL import Image
import json
import numpy as np
#import preproc_beta
import os
import datetime


##THIS ONE TAKES 2 ms


def dist(f, t):
	return int((abs(f[0]-t[0])**2 + abs(f[1]-t[1])**2 + abs(f[2]-t[2]))**0.5)

def unimportant(rgb):
	return (rgb[0] <= 200 and rgb[1] <= 200 and rgb[2] <= 200) or (rgb[1] > 200 and rgb[2] > 200 and rgb[2] >= rgb[1])

slot_state = np.zeros((14,13))
hops = []
final_list = []
cd = [0,0]

tt = Image.open(input("Enter file path: ")).rotate(180)
#tt = Image.open("ttpxt.png")

#print(datetime.datetime.time(datetime.datetime.now()))

dim = tt.size

def updateNPCoord():
    global cd
    if cd[1] < 12:
        cd = [cd[0], cd[1]+1]
    else:
        cd = [cd[0]+1, 0]

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
		rgb = tt.getpixel((i,j))
		if unimportant(rgb) == False:
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
			RGB = tt.getpixel((i,j))
			if unimportant(RGB) == False:
				if dist((203,254,51), RGB) < dist((255,255,204), RGB):
					slot_state[cd[0], cd[1]] = 1

			updateNPCoord()

			if a == 12:
				break
			
			if b == 0:
				h = 1
				i = i + 1
				while unimportant(tt.getpixel((i,j))) == False:
					i = i + 1
					h = h + 1
				while unimportant(tt.getpixel((i,j))) == True:
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
		while unimportant(tt.getpixel((i,j))) == False:
			j = j + 1
		while unimportant(tt.getpixel((i,j))) == True:
			j = j + 1

except IndexError:
	if cd[0] < 10 or cd[1] != 0:
		x = input("BAD FILE: Please upload a proper time table image...")
		exit()

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

#print(datetime.datetime.time(datetime.datetime.now()))
#os.remove("ttpxt.png")
print(json.dumps(final_list))
x = input("\nGive any input to continue...")
exit()
