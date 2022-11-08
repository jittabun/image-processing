# เปิดกล้องด้วย Opencv
import cv2 

cap = cv2.VideoCapture(0) # เปิดกล้อง

while True:
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    cv2.imshow('Output' , frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release() # Clear ram
cv2.destroyAllWindows()
