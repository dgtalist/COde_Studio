import cv2
import motor_module as motor
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Frame_Width  = 640
Frame_Height = 480
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,  Frame_Width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Frame_Height)

try:
    while True:
        (_, frame) = camera.read()
        frame = cv2.GaussianBlur(frame, (11, 11),1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red=cv2.inRange(hsv,(0,100,100),(5,255,255))
        upper_red=cv2.inRange(hsv,(170,100,100),(180,255,255))
        mask=cv2.addWeighted(lower_red,1.0,upper_red,1.0,0.0)
        
        mask = cv2.erode(mask, None, iterations=2) #Do erode if needed
        #mask = cv2.dilate(mask, None, iterations=2) # Do dilate if needed
        # Find the contours
        #_, contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        center = None
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea) # Find the max length of contours
            ((x, y), radius) = cv2.minEnclosingCircle(c) # Find the x, y, radius of given contours
            M = cv2.moments(c) # Find the moments

            try:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) # mass center
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2) # process every frame
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        
                # Forward, backward, Turn rules
                # Size of the recognized object           
                """
                if radius < 25 and radius > 5 :
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                    elif center[0] < Frame_Width/2 -55 : #turnLeft_Area Set
                        motor.turnLeft()
                    else:
                        print(radius) """
                if  radius > 5 :
                    motor.forward_1()
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                    elif center[0] < Frame_Width/2 -55 :
                        motor.turnLeft()
                    else:
                        motor.forward_1() #Low Run
                    #elif radius > 65:
                    #    motor.Reverse()
                else:
                    motor.brake()
            except:
                pass
        else:
            motor.stop()
        cv2.imshow("Frame", frame)  # if you don't need to display and the car will get faster
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
finally: #except KeyboardInterrupt:
    motor.cleanup()
    camera.release()
    cv2.destroyAllWindows()
