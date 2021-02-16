import numpy as np
import cv2 as cv
from PIL import Image 

#img = cv.imread("./Filled/test9.png")
im = np.array(Image.open("./Filled/test6.png").convert("RGB"))
im2 = np.array(Image.open("./Vessel/test6.png").convert("RGB"))
 
sought = [255,0,255]

result1 = np.count_nonzero(np.all(im==sought,axis=2))
result2 = np.count_nonzero(np.all(im2==sought,axis=2))
answer = (result1/result2) * 100
print("The container is {value:.2f}% filled".format(value=answer))
