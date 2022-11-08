import cv2
img = cv2.imread(r"C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\cat.jpg")

cv2.imshow("output" , img) # show_picture(title , img)
cv2.waitKey(delay = 5000) # เปิด 5 วิ
cv2.destroyAllWindows()