import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
scale = 9
imgrows, imgcols = int(img.shape[0]*scale), int(img.shape[1]*scale)
timgrows, timgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
imgc = nump.zeros((imgrows, imgcols, rgb), dtype=int)

scale = scale
z = 0
# countx = 0
# county = 0
# trix = 0
# triy = 0
# imgrows = int(imgrows * 2)
# imgcols = int(imgcols * 2)
for x in range(imgrows):
    # county = 0
    # if trix == scale and countx < timgrows:
    #     countx = countx + 1
    #     trix = 0
    # else:
    #     trix = trix + 1

    for y in range(imgcols):
        # if triy == scale and county < timgcols:
        #     county = county + 1
        #     triy = 0
        # else:
        #     triy = triy + 1

        if z == 0:
            imgc[x,y,:] = img[int(x / scale), int(y/scale),:]
            z=z+1
        elif z == 3:
            imgc[x,y,:] = 0
            z=0
        else:
            imgc[x,y,:] = 0
            z = z+1





# plt.imshow(imgc), plt.show()
imgc = imgc.astype(nump.uint8)
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwanglebig.jpeg", imgc)
