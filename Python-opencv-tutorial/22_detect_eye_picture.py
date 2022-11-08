import cv2

# impeor picture
img = cv2.imread(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\girl.jpg')

#read file for classification
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\Detect\haarcascade_eye_tree_eyeglasses.xml')

# Use gray image to eye classification
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#face Classification
scaleFactor = 1.1
minNeighber = 3
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

# แสดงตำแหน่งที่เจอดวงตา
for (x,y,w,h) in eye_detect:
    cv2.rectangle(img ,(x,y),(x+w,y+h),(0,255,0),thickness=5)


# แสดงภาพ
cv2.imshow('original' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()