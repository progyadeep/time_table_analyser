'''
This code implements a more general way to come across table cells. It now compares colours with RGB value ranges
instead of absolut values like the previous version.

Produces a json array as ouput..

#################################################################################
#									        #
#   B E T A   V E R S I O N   : : :   U S E   A T   Y O U R   O W N   R I S K   #
#   _________________________________________________________________________	#
#										#
#   This code has not undergone adequate testing/training, so it is not		#
#   guaranteed to work in 100% of the cases. >>> Old Readme applies <<<		#
#										#
#################################################################################
'''

from PIL import Image
import json
import numpy as np

slot_state = np.zeros((14,13))
final_list = []
cd = [0,0]
tt = Image.open("tt_shreyash.jpg")

dim = tt.size


def isLine(t):
	return t[0] < 200 and t[1] < 200 and t[2] < 200


def isGreen(p):
	return p[0] > 190 and p[1] > 200 and p[2] < 100
	

def isBOY(p):
	return (p[0] > 240 and p[1] > 230) and ((p[2] > 100 and p[2] < 200) or p[2] > 200) and (p[2] < p[0] and p[2] < p[1])


def updateNPCoord():
    global cd
    if cd[1] < 12:
        cd = [cd[0], cd[1]+1]
    else:
        cd = [cd[0]+1, 0]


cols = ((203, 254, 51), (255, 255, 203), (248, 239, 164))
        #filled           emptyTH         empty LAB

start = [] ##coordinates of the starting point

i=0
while i < dim[0]:
    j = 0
    while j < dim[1]:
        rgb = tt.getpixel((i,j))
        if isGreen(rgb) or isBOY(rgb):
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
			if isGreen(tt.getpixel((i,j))):
				slot_state[cd[0], cd[1]] = 1
			
			updateNPCoord()

			if a == 12:
				break

			i = i + 1
			while not isLine(tt.getpixel((i,j))):
				i = i + 1
			while not isGreen(tt.getpixel((i,j))) and not isBOY(tt.getpixel((i,j))):
				i = i + 1

    	#printing
    	#for x in range(13):
    	#    print(int(slot_state[b][a]), end=' ')
    	#print('\n')

		if b == 13:
			break


		i = start[0]
		j = j + 1
		while not isLine(tt.getpixel((i,j))):
			j = j + 1
		while not isGreen(tt.getpixel((i,j))) and not isBOY(tt.getpixel((i,j))):
			j = j + 1

except IndexError:
	if cd[0] < 9:
		print("BAD FILE: Please upload a proper time table image.")
		exit()

a = 0
while a < 13:
    b = 0
    while b < 13:
        final_list.append(int(slot_state[a,b] + slot_state[a+1, b]))
        b = b + 1
    a = a + 2

print("\n"+json.dumps(final_list))
