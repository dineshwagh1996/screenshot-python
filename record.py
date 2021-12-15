import cv2
import tkinter as tk
import numpy as np
import pyautogui
from tkinter.filedialog import asksaveasfilename
import time
import datetime
import sys
from threading import *


class recordfun(Thread):
 def run(self):
  print("recording!!")
  while True:

    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = pyautogui.size()
    currenttime=time.time()
    # rm=str(currenttime)
    dt= datetime.datetime.now()
    d=dt.strftime("%b-%d-%y_%H-%M-%S")
    rem=str(d)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    file_name=(r'C:\Users\USER\Desktop\recorddata\record'+rem+'.avi')
    # file_name = asksaveasfilename(confirmoverwrite=False,defaultextension='.avi')
    out = cv2.VideoWriter(file_name, fourcc, 20.0, (SCREEN_SIZE))
    print("Recording Started...\n")
    odd=1
    while True:
        odd+=1
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if(odd==10):
            # cv2.imshow("Recording...", frame)
            odd=1
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            break
        # write the frame

    out.write(frame)
    out.release()
    root.destroy()
    sys.exit(0)

t1=recordfun()
t1.start()
