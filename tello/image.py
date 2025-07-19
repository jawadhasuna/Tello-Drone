from djitellopy import tello
import cv2
mine = tello.Tello()
mine.connect()
print(mine.get_battery())
mine.streamon()
while True:
    img=mine.get_frame_read().frame
    img= cv2.resize(img, (360,240))
    cv2.imshow("image",img)
    cv2.waitKey(1)