#แสดงวันเวลาในกล้อง/วิดีโอ
import cv2 
import datetime
# cap = cv2.VideoCapture(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\Video.mp4') #ตำแหน่งเก็บvideo
cap = cv2.VideoCapture(0) #แสดงในกล้อง

while (cap.isOpened()): # เช็คว่าวีดิโอไม่พัง
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame, currentDate, (10 , 30) , cv2.FONT_HERSHEY_SIMPLEX , 0.8 , (0,255,0) , cv2.LINE_4) # add text on clip video
        cv2.imshow('Output' , frame)
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break
    else :
        break

cap.release() # Clear ram
cv2.destroyAllWindows()