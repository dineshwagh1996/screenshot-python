from PIL import ImageGrab
import os
from datetime import datetime
import threading
import random
import ftplib


def screenshot():
    name = random.randint(0, 1000)
    print(name)
    if os.path.isdir(str(name)) is False:
        name = random.randint(0, 1000)
        name = str(name)

    name = os.path.join(os.getcwd(), str(name))
    print("ALl logs saved in dir:", name)
    os.mkdir(name)
    while True:
        os.chdir(name)
        im = ImageGrab.grab([320, 180, 1600, 900])
        dt = datetime.now()
        fname = "pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
        im.save(fname, 'png')

t1=threading.Thread(target=screenshot,)
t1.start()
