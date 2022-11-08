import cv2

img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg")
imgresize = cv2.resize(img , (700,700))

#วาดภาพบนข้อความ
# putText(ภาพ , ข้อความ , พิกัดแสดงข้อความ (x,y) , font ,ขนาดข้อความ , สี, ความหนา)

cv2.putText(imgresize , "CAT" , (150,400) , cv2.FONT_HERSHEY_SIMPLEX , 2.5 , (0,0,255) ,cv2.LINE_4)

cv2.imshow('Output' , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()