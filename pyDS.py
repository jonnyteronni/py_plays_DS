import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
import directkeys_linux as dkey

# Region of interest
def roi(img,vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img,mask)
    return masked

# Put screen only in grey lines
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=150, threshold2=160)
    #vertices = np.array([[450,300],[300,300],[600,300],[600,450]])
    #vertices = np.array([[0,0],[800,450],[0,450],[800,0]])
    vertices = np.array([[800,450],[0,450],[400,300]])
    processed_img = roi(processed_img,[vertices])
    return processed_img



# Waiting for selecting the game window
# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)


# walking for 3 seconds
# print('Walking for 3 seconds')
# dkey.sendkeys_down('w')
# time.sleep(3)
# dkey.sendkeys_up('w')
# print('Walking back for 3 seconds')
# dkey.sendkeys_down('s')
# time.sleep(3)
# dkey.sendkeys_up('s')



# TODO: Comment everything
sct = mss()
last_time = time.time()
while 1:
    w, h = 800, 450
    monitor = {'top': 65, 'left': 0, 'width': w, 'height': h}
    screen = np.array(Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb))
    #screen = np.array(sct.grab(monitor).rgb)
    new_screen = process_img(screen)
    cv2.imshow('window1',new_screen)

    #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_RGB2BGR))
    print('Loop took {} seconds.'.format(time.time()-last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
