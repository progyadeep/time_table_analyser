from PIL import Image

im = Image.open(input("Enter file path: "))

def dist(f, t):
	return int((abs(f[0]-t[0])**2 + abs(f[1]-t[1])**2 + abs(f[2]-t[2]))**0.5)

d = im.size
out = Image.new('RGB', d, (255,255,255))
r = 190
for i in range(d[0]):
	for j in range(d[1]):
		p = im.getpixel((i,j))
		if p[0] <= 200 and p[1] <= 200 and p[2] <= 200: #preprocessing 1
			out.putpixel((i,j), (0,0,0))
		elif p[1] > 200 and p[2] > 200 and p[2] >= p[1]: #preprocessing 2
			out.putpixel((i,j), (0,0,200))
		else: #preprocessing 3 (monotonizing 2)
			dg = dist((203,254,51), p)
			dy = dist((255,255,204), p)
			if dg < dy:
				out.putpixel((i,j), (0,255,0))
			else:
				out.putpixel((i,j), (255,255,0))


out.rotate(180).save("ttpxt.png")
