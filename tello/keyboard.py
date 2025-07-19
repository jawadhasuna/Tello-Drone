import keymodule as kp
from djitellopy import tello
from time import sleep
import cv2

kp.init()
me = tello.Tello()
me.connect()
print("Battery:", me.get_battery())

me.streamon()  # ✅ Start the video stream ONCE

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed
    if kp.getKey("q"):
        me.land()
        sleep(3)
    if kp.getKey("e"):
        me.takeoff()
    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    # ✅ Get and display frame
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Tello Video", img)

    # ✅ Allow ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        me.land()
        break

cv2.destroyAllWindows()
