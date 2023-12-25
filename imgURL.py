import cvzone
import cv2

cap=cv2.VideoCapture(0)
imgURL=cvzone.downloadImageFromUrl(url='https://opencv1.b-cdn.net/wp-content/uploads/2022/05/logo.png', keepTransparency=True)
while True:
    success,img=cap.read()
    imgOverlay=cvzone.overlayPNG(img,imgURL,pos=[20,20])
    cv2.imshow("overlay img",imgOverlay)
    cv2.waitKey(1)