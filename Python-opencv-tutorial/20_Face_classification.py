import cv2

# impeor picture
img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\boy.jpg')

#read file for classification
face_cascade = cv2.CascadeClassifier(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\Detect\haarcascade_frontalface_default.xml')

# Use gray image to face classification
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#face Classification
scaleFactor = 1.1
minNeighber = 3
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

# แสดงตำแหน่งที่เจอใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img ,(x,y),(x+w,y+h),(0,255,0),thickness=5)


# แสดงภาพ
cv2.imshow('original' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()