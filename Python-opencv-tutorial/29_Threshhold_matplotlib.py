#ฟังก์ชั่น threshold ใน opencv with mathplotlib

import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\gradient.png')

# thresh = จุดแบ่ง , th = ค่าที่ได้
thresh , th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh , th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh , th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC) # ถ้าค่าสูงกว่าจุดแบ่ง ให้เท่ากับจุดแบ่งที่เหลือเท่าเดิม
thresh , th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO) # ถ้าตำ่กว่าจุดแบ่งเปลี่ยนเป็นศูนย์ที่เหลือคงเดิม
thresh , th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV) # ถ้าสูงกว่าจุดแบ่งเปลี่ยนเป็นศูนย์ที่เหลือคงเดิม


# cv2.imshow("Original", gray_img)
# cv2.imshow("Binary" , th1)
# cv2.imshow("Binary_INV" , th2)
# cv2.imshow("Trunc" , th3)
# cv2.imshow("TOZERO" , th4)
# cv2.imshow("TOZERO_INV" , th5)

images = [gray_img,th1,th2,th3,th4,th5]
titles = ['Output' , 'Binary', 'Binary_INV', 'Trunc' , 'TOZERO' ,'TOZERO_INV' ]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()