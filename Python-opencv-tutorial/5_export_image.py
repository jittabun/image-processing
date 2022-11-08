#การเขียนภาพ
import cv2
img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg" , 0)
imgresize = cv2.resize(img ,(400,400))

cv2.imwrite("output.jpg" , imgresize)

#แสดงภาพ
cv2.imshow("output" , imgresize) # show_picture(title , img)
cv2.waitKey(0) 
cv2.destroyAllWindows()