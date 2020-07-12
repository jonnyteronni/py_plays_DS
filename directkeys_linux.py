# from: https://stackoverflow.com/questions/9681959/how-can-i-use-xdotool-from-within-a-python-module-script
# https://github.com/rshk/python-libxdo/blob/master/xdo/__init__.py

import sys
from xdo import Xdo
from time import sleep

def sendkeys_down(*keys):
    for k in keys: xdo.send_keysequence_window_down(0, k.encode())

def sendkeys_up(*keys):
    for k in keys: xdo.send_keysequence_window_up(0, k.encode())


def type(text):
    xdo.enter_text_window(0, text.encode())

#sleep(0.5)
xdo = Xdo()

# this updates a row in a spreadsheet with copies from prior row
# first check that this is the intended spreadsheet
# if 'Trades' in xdo.get_window_name(xdo.get_active_window()).decode():
#     with open('my_data_file_name', 'r') as f:
#         trade = (f.readlines()[-int(sys.argv[1])])[:-1]
#         t = [s if s else '0' for s in trade.split('\t')]
#         type('\t'.join(t[:7]))
#         sendkeys('Tab', 'Up', 'ctrl+c', 'Down', 'ctrl+v', 'Right')
#         type(' ' + t[-3])
#         sendkeys('Tab')
#         type(t[-2])
#         sendkeys('Tab')
#         type(t[-1])
#         sendkeys('Tab', 'Up', 'ctrl+c', 'Down', 'ctrl+v', 'Right')
#         type('333')
#         sendkeys('Tab')
