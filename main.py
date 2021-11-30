import cv2
import numpy as np
import pyws as m
import win32
import win32gui
from PIL import ImageGrab
import pyautogui
from pyautogui import screenshot
target_class = 0
target_name  = 'Discord'

try :
    handle =  win32gui.FindWindow(target_class , target_name)

    rect   =  win32gui.GetWindowRect(handle)

    image=ImageGrab.grab(rect)
    image.show()
    image.save('001.png')
except IndexError as e:

        '''img = ImageGrab.grab(rect)
        img = np.asarray(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        cv2.imwrite('001.jpg',img)
        cv2.imcv2.imwrite('/D:/NIT/001/OneDrive - 77r6sw/00py' + datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg', img)
     

screenshot = pyautogui.screenshot(region = (handle))
screenshot.save('スクリーンショット.png')   '''