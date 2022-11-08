#เปลี่ยนสีการนำเข้าภาพ
import cv2
img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg" , 0)
imgresize = cv2.resize(img , (400,400))

#แสดงภาพ
cv2.imshow("output" , imgresize) # show_picture(title , img)
cv2.waitKey(delay = 5000) 
cv2.destroyAllWindows()