from PIL import Image

im = Image.open(input("Enter file path: "))

#preprocessing 1

d = im.size
out = Image.new('RGB', d, (255,255,255))
r = 190
for i in range(d[0]):
	for j in range(d[1]):
		p = im.getpixel((i,j))
		if p[0] <= 200 and p[1] <= 200 and p[2] <= 200:
			out.putpixel((i,j), (0,0,0))
		else:
			out.putpixel((i,j), p)

out.save("ttpxt.png")


#preprocessing 2

im = Image.open("ttpxt.png")

def dist(f, t):
	return int((abs(f[0]-t[0])**2 + abs(f[1]-t[1])**2 + abs(f[2]-t[2]))**0.5)

out = Image.new("RGB", d, (0,0,0))

for a in range(d[0]):
	for b in range(d[1]):
		rgb = im.getpixel((a,b))
		if rgb != (0,0,0):
			if rgb[1] > 200 and rgb[2] > 200 and rgb[2] >= rgb[1]:
				out.putpixel((a,b), (0,0,200))
			else:
				out.putpixel((a,b), rgb)

out.save("ttpxt.png")

#preprocessing 3 (monotonizing 2)

im = Image.open("ttpxt.png")
out = im

a,b=0,0
for a in range(d[0]):
	for b in range(d[1]):
		rgb = im.getpixel((a,b))
		if rgb != (0,0,0) and rgb != (0,0,200):
			dg = dist((203,254,51), rgb)
			dy = dist((255,255,204), rgb)
			if dg < dy:
				out.putpixel((a,b), (0,255,0))
			else:
				out.putpixel((a,b), (255,255,0))

out.rotate(180).save("ttpxt.png")
