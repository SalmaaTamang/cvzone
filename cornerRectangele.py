import cv2
import cvzone
cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    cvzone.cornerRect(img,(200,200,350,200)) #(x,y width ,height coordinate are given)
    cvzone.putTextRect(img,"Merry Chrismas",(200,200))
    # cv2.rectangle(img,(200,200),(500,400),(255,0,0),3)
    cv2.imshow("Video",img)
    cv2.waitKey(1)

  