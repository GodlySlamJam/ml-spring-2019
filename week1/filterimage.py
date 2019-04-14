import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
imgrows, imgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
filtered = nump.zeros((imgrows, imgcols, rgb), dtype=int)
blur=nump.array(([1,2,1],[0,0,0],[-1,-2,-1]))


print(blur[0][1])
holdcell = filtered
xl = 0
yl = 0
for x in range(3,imgrows-3):
    xl=x+3
    for y in range(3,imgcols-3):
        yl = y+3
        holdcell[x:xl,y:yl] = img[x:xl,y:yl]
        filtered[x:xl,y:yl] = holdcell[x,y:yl] @ blur
        # for z in range(2):
        #     for a in range(0,2):

                # if a + y < imgcols:
                #     filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[0][:]
                # else:
                #     filtered[x+z,y,:] = filtered[x+z,y,:]*blur[0][:]
                # if z + x < imgrows:
                #     filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[0][:]
                # else:
                #     filtered[x,y+a,:] = filtered[x,y+a,:]*blur[0][:]
                #
                # filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[a][:]

plt.imshow(filtered), plt.show()
filtered = filtered.astype(nump.uint8)
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwangleblurry.jpeg", filtered)
