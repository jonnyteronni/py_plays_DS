import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
import directkeys_linux as dkey

# Put screen only in grey lines. Not working.
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

# Waiting for selecting the game window
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


# walking for 3 seconds
print('Walking for 3 seconds')
dkey.sendkeys_down('w')
time.sleep(3)
dkey.sendkeys_up('w')
print('Walking back for 3 seconds')
dkey.sendkeys_down('s')
time.sleep(3)
dkey.sendkeys_up('s')

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
