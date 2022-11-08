# detect eye on video
import cv2 

cap = cv2.VideoCapture(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\Mark.mp4') #ตำแหน่งเก็บvideo

eye_cascade = cv2.CascadeClassifier(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\Detect\haarcascade_eye_tree_eyeglasses.xml')

while (cap.isOpened()): # เช็คว่าวีดิโอไม่พัง
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        # Use gray image to face classification
        gray_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        #face Classification
        scaleFactor = 1.1
        minNeighber = 3
        eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
        # แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in eye_detect:
            cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow('Output' , frame)
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break
    else :
        break

cap.release() # Clear ram
cv2.destroyAllWindows()
