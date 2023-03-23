import time
import cv2
import random
import string
import os



from conf.config import Config


  
# define a video capture object
conf = Config()
TIMER = conf.TIMER
cam = cv2.VideoCapture(conf.CAM_PORT)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)   
while(True):
     
    # Capture the video frame
    # by frame
    ret, frame = cam.read()
  
    # Display the resulting frame
    cv2.imshow('Joyeux noel Gwen !', frame)
    
    
    if cv2.waitKey(125) & 0xFF == ord(' '): 
        prev = time.time()
        while TIMER >= 0:
            ret, frame = cam.read()
 
            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, str(TIMER),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('Joyeux noel Gwen !', frame)
            cv2.waitKey(125)
 
            # current time
            cur = time.time()
 
            # Update and keep track of Countdown
            # if time elapsed is one second
            # then decrease the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
 
        else:
            ret, frame = cam.read()
            TIMER = conf.TIMER
            # Display the clicked frame for 2
            # sec.You can increase time in
            # waitKey also
            cv2.imshow('Joyeux Noel Dodo', frame)
 
            # time for which image displayed
            cv2.waitKey(2000)

        
            imgName = res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            fileName = conf.IMAGE_PATH + imgName + ".jpg"
            exist = os.path.exists(fileName)
            if not exist:
                cv2.imwrite(fileName, frame)	
                originalImage = cv2.imread(fileName)
                grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
                fileName = conf.IMAGE_PATH + imgName + "BandW.jpg"
                cv2.imwrite(fileName, grayImage)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()

