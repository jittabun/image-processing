import cv2

#อ่านภาพไฟล์
img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img , (700 , 700))


#วาดเส้นตรง
# ractangle(ภาพ, มุม1(บนซ้าย) , มุม2(ล่างขวา) , สี , ความหนา) ความหนา -1 คือเติมที่ในวงกลม

cv2.rectangle(imgresize ,(100,100) , (500,500) , (0,0,255),-1)

cv2.imshow('output' , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()