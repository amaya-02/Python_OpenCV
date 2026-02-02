#!/usr/bin/env python3

######### Task 1 ##########
# Create a class VideoPlayer. The class must have:
# 1. A constructor
# 2. One class method to display the frames
###########################
import numpy as np
import cv2 as cv
import os 

class VideoPlayer:
    def __init__(self):
        cdir=os.getcwd()
        self.cap=cv.VideoCapture(cdir+"/src/test_video.mp4") # reads video file

    def dispFrames(self):
        if not self.cap.isOpened(): # if vid is not ok
            print("can't open video.") 
            exit() # if it is


        # read & display frames
        while True: 
            #returns boolean & frame
            ret,frame = self.cap.read()

            if not ret: # if vid don't start or ends
                print("can't recieve frame.")
                break
            
            # displays frame
            cv.imshow('frame', frame)

            # to leave early press q
            if cv.waitkey(1)==ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()

    
def main():
    myVideo= VideoPlayer()
    myVideo.dispFrames()

if __name__=="__main__":
    main()