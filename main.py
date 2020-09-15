import cv2
img = cv2.imread('lenna.png',1)
cv2.imshow('lenna',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('lenna_test.png',img)
