# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# %%
def normalize(plane):
    imin = np.percentile(plane,1)
    imax = np.percentile(plane,99)
    return np.clip((plane - imin) / (imax - imin),0,1)


# %%

img = cv.imread("IMG_3064.jpeg")
# assert(img != None)
bneg,gneg,rneg = cv.split(img)
    
b,g,r = 1-normalize(bneg), 1-normalize(gneg), 1-normalize(rneg)
new_img = (cv.merge([b,g,r]) * 255).astype(np.uint8)
    #new_img = cv.fastNlMeansDenoisingColored(new_img,None,10,17,7,15) #h,hcolor,tempalteWindowSize,searchWIndowSize
    
    #plt.imshow(new_img)
    #plt.show()
    
cv.imwrite("positive_image4.jpeg",new_img)

# %%



