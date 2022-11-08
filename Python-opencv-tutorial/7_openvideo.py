# เปิดvideoด้วย Opencv
import cv2 

cap = cv2.VideoCapture(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\Video.mp4') #ตำแหน่งเก็บvideo

while (cap.isOpened()): # เช็คว่าวีดิโอไม่พัง
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        cv2.imshow('Output' , frame)
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break
    else :
        break

cap.release() # Clear ram
cv2.destroyAllWindows()
