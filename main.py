import cv2 as cv
import numpy as np

def mask_by_color_range(img, lower, upper):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    return mask


img = cv.imread('luffa/luffa5.jpg')
if img is not None:
    img = cv.resize(img, (800, 600))

    lower_blue = np.array([30,40,0])
    upper_blue = np.array([70,255,255])
# Threshold the HSV image to get only blue colors
    mask = mask_by_color_range(img, lower_blue,upper_blue)
    cv.imshow('image', mask)
    blur = cv.bilateralFilter(img, 9, 90, 90)
    mask2 = mask_by_color_range(blur, lower_blue, upper_blue)

    cv.imshow('image2', mask2)
    key = cv.waitKey(0)

    
    print(img[0,0])
    print(type(img[0,0]))

cv.destroyAllWindows()
