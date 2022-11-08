#Laparcian Method
import cv2
img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\currency.jpg',0)

lap = cv2.Laplacian(img,-1)

cv2.imshow("Output",img)
cv2.imshow("Output",lap)

cv2.waitKey(0)
cv2.destroyAllWindows()