import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
imgrows, imgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
red = nump.zeros((imgrows, imgcols, rgb), dtype=int)

for x in range(imgrows):
    for y in range(imgcols):
        tint = sum(img[x, y, :]) /3
        red[x,y,:] = tint

plt.imshow(red), plt.show()
red = red.astype(nump.uint8)
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwanglegrey.jpeg", red)
