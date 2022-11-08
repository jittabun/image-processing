#ฟังก์ชั่น threshold ใน opencv

import cv2
gray_img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\gradient.png')

# thresh = จุดแบ่ง , th = ค่าที่ได้
thresh , th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh , th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh , th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC) # ถ้าค่าสูงกว่าจุดแบ่ง ให้เท่ากับจุดแบ่งที่เหลือเท่าเดิม
thresh , th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO) # ถ้าตำ่กว่าจุดแบ่งเปลี่ยนเป็นศูนย์ที่เหลือคงเดิม
thresh , th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV) # ถ้าสูงกว่าจุดแบ่งเปลี่ยนเป็นศูนย์ที่เหลือคงเดิม


cv2.imshow("Output", gray_img)
cv2.imshow("Binary" , th1)
cv2.imshow("Binary_INV" , th2)
cv2.imshow("Trunc" , th3)
cv2.imshow("TOZERO" , th4)
cv2.imshow("TOZERO_INV" , th5)
cv2.waitKey(0)
cv2.destroyAllWindows()