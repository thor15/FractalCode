import math
from PIL import Image

#Define needed variables
WIDTH = 800
MAX_INTERATIONS = 80
VALUEZ = []
SCALE = 300
cConstant = complex(.4,.21)

#For the Broken Image
#change = 300
#midA = 0
#midB = -52

#For the Normal Image
#change = 400
#midA = 0
#midB = -52



change = 300
midA = 0
midB = -52

#Define my wanted boundries for the image
a1 = (midA-change)/SCALE
a2 = (midA+change)/SCALE
b1 = (midB-change)/SCALE
b2 = (midB+change)/SCALE

#Define the scale needed to have 800 points between the begining and the end
aDivisor = (abs(a2-a1)/WIDTH)
bDivisor = (abs(b2-b1)/WIDTH)
aScale = int(pow(aDivisor, -1))
bScale = int(pow(bDivisor, -1))

#Scale a and b so that they have the correct range
a1f = a1*aScale
a2f = a2*aScale
b1f = b1*bScale
b2f = b2*bScale

#Define teh juliaSet Function
def juliaSet(c):
    z = c
    step = 0
    while(abs(z) <= 2 and step < MAX_INTERATIONS):
        #print(step)
        z = z*z + cConstant
        step += 1
    return step

#Main Part, loops over a and b values to compute the image
for a in range(math.floor(a1f), math.ceil(a2f), 1):
    for b in range(math.floor(b1f), math.ceil(b2f), 1):
        c = complex((a/aScale), (b/bScale))
        e = juliaSet(c)
        VALUEZ.append(e)
        

width = int(math.sqrt(len(VALUEZ)))
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,WIDTH-1-y], (int(VALUEZ[x*WIDTH+y]*255/MAX_INTERATIONS),int(VALUEZ[x*WIDTH+y]*255/MAX_INTERATIONS),int(VALUEZ[x*WIDTH+y]*255/MAX_INTERATIONS)))

#Show and save the image
img.show()
fileN = 'BrokenImage.png'
img.save(fileN)