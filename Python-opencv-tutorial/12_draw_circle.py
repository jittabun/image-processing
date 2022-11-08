import cv2

#อ่านภาพไฟล์
img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img , (700 , 700))


#วาดเส้นตรง
# circle(ภาพ, จุดศูนย์กลาง (x,y) , รัศมี , สี , ความหนา)

cv2.circle(imgresize , (200,200) , 70 ,(0,0,255) , 7)

cv2.imshow('output' , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()