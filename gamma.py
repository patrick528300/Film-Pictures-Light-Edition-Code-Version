# %%
import cv2
import numpy as np

# %%
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

# %%
folder = "vintage_market_SD_122025/"
i = 15
image = cv2.imread(folder+"0000000100"+str(i)+".jpg")
new_image = adjust_gamma(image,0.7)
cv2.imwrite(folder+"newImage"+str(i)+".jpg",new_image)


