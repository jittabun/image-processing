# เปิดvideoด้วย Opencv
import cv2 

cap = cv2.VideoCapture(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\Mark.mp4') #ตำแหน่งเก็บvideo

#read file for classification
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\Detect\haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\Detect\haarcascade_frontalface_default.xml')

while (cap.isOpened()): # เช็คว่าวีดิโอไม่พัง

    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame

    if check == True:
        gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        #face Classification
        scaleFactor = 1.1
        minNeighber = 3
        face_detect = face_cascade.detectMultiScale(gray_frame,1.3,4)
        eye_detect = eye_cascade.detectMultiScale(gray_frame,scaleFactor,minNeighber)

        # แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            for (ex,ey,ew,eh) in eye_detect:
                cv2.rectangle(frame ,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)
                
        cv2.imshow('Output' , frame)
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break
    else :
        break

cap.release() # Clear ram
cv2.destroyAllWindows()
