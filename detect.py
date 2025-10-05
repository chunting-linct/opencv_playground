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
def blur_with_edge(img):
    return cv.bilateralFilter(img, 9, 120, 120)

if __name__ == '__main__':
    img = cv.imread('luffa/luffa5.jpg')
    if img is not None:
        img = cv.resize(img, (800, 600))

        lower_blue = np.array([30,40,0])
        upper_blue = np.array([70,255,255])
        mask = mask_by_color_range(img, lower_blue,upper_blue)
        edges = cv.Canny(img, 100, 500)
        contours, hierachy = cv.findContours(mask, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        approx_con = []
        for c in contours:
            eps = cv.arcLength(c, True) * 0.01
            approx_con.append(cv.approxPolyDP(c, eps, True))
        images = cv.drawContours(img, approx_con, -1, (0,255,0), 3)

        #cv.imshow('image2', images)
        images = cv.drawContours(img, contours, -1, (0,255,0), 3)

        #cv.imshow('image3', images)
        calculate_hue_hist(img)
        #cv.imshow('image3', images)
        key = cv.waitKey(0)


        

    cv.destroyAllWindows()
