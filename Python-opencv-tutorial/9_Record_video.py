# record video from camera
import cv2 

cap = cv2.VideoCapture(0) # เปิดกล้อง

fourcc = cv2.VideoWriter_fourcc(*'XVID') #นามสกลุลvideo

result = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480)) #export video

while True:
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    if check == True:
        cv2.imshow('Output' , frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break

result.release()
cap.release() # Clear ram
cv2.destroyAllWindows()
