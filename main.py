import cv2 as cv
import numpy as np

def mask_by_color_range(img, lower, upper):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    return mask


img = cv.imread('luffa/luffa3.jpg')
if img is not None:
    lower_blue = np.array([30,40,50])
    upper_blue = np.array([70,255,255])
# Threshold the HSV image to get only blue colors
    mask = mask_by_color_range(img, lower_blue,upper_blue)
    mask = cv.resize(mask, (800, 600))

    cv.imshow('image', mask)
    key = cv.waitKey(0)

    
    print(img[0,0])
    print(type(img[0,0]))

cv.destroyAllWindows()
