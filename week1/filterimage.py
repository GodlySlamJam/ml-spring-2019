import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
imgrows, imgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
filtered = nump.zeros((imgrows, imgcols, rgb), dtype=int)
blur=[0.75,0.65,0.75],[0.65,0.75,0.65],[0.75,0.65,0.75]


print(blur[0][1])

for x in range(3,imgrows-1):
    for y in range(3,imgcols-1):
        for z in range(0,rgb-1):
            for a in range(0,2):
                # if a + y < imgcols:
                #     filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[0][:]
                # else:
                #     filtered[x+z,y,:] = filtered[x+z,y,:]*blur[0][:]
                # if z + x < imgrows:
                #     filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[0][:]
                # else:
                #     filtered[x,y+a,:] = filtered[x,y+a,:]*blur[0][:]

                filtered[x+z,y+a,:] = filtered[x+z,y+a,:]*blur[a][:]


plt.imshow(filtered), plt.show()
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwangleblurry.jpeg", filtered)
