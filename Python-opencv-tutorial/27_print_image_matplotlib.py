#แสดงผลด้วย matplotlib
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\girl.jpg')
cv2.imshow('Output' , img)

img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()