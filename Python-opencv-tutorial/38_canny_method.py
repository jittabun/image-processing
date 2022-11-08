# Canny Method
import cv2

img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\currency.jpg',0)
canny = cv2.Canny(img,50,200)

cv2.imshow('Original' , img)
cv2.imshow('Canny' , canny)
cv2.waitKey()
cv2.destroyAllWindows()