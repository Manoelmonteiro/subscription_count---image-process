import cv2 as cv
import matplotlib.pyplot as plt

filename = '1.png'
src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
plt.imshow (src,cmap='gray')
plt.show()



dst = src.copy()
dst[dst<140]=0
dst[dst>0]=255

plt.imshow (dst,cmap='gray')