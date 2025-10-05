import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

def mask_by_color_range(img, lower, upper):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    return mask


def calculate_hue_hist(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0], None, [180], [0, 180])
    plt.plot(hist)
    plt.show()


if __name__ == '__main__':
    img = cv.imread('luffa/luffa5.jpg')
    if img is not None :
        ref = img[800: 1200, 600 : 650]
        cv.imshow('image3', ref)
        key = cv.waitKey(0)
        img = cv.resize(img, (800, 600))
        hsv = cv.cvtColor(ref, cv.COLOR_BGR2HSV)
        hsvt = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        refhist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0,180,0,256])
        cv.normalize(refhist, refhist,0,255,cv.NORM_MINMAX)
        bp = cv.calcBackProject([hsvt], [0, 1], refhist, [0,180,0,256], 1)

        cv.imshow('image3', bp)
        key = cv.waitKey(0)
        

        

    cv.destroyAllWindows()
