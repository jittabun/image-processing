# เปิดvideoด้วย Opencv
import cv2 

cap = cv2.VideoCapture(r'C:\Users\Jittabun\Desktop\Pom_practice\Python-opencv-tutorial\image\Video.mp4') #ตำแหน่งเก็บvideo

while (cap.isOpened()): # เช็คว่าวีดิโอไม่พัง
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # เปลี่ยนสีจาก frame ให้เป็นสีเทา
        cv2.imshow('Output' , gray) # โชว์ภาพ
        if cv2.waitKey(1) & 0xFF == ord('e'): #กดตัว e เพื่อออก
            break
    else :
        break

cap.release() # Clear ram
cv2.destroyAllWindows()
