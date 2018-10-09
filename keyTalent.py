import win32gui
import win32process
import win32api
import win32con
import time
import keycode
classname = "Notepad"
keys=123
VKCODE ={}
#获取句柄
def callback(hwnd, hwnds):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        classid = win32gui.GetClassName(hwnd)
        #print(classid)
        if classid == classname :
            hwnds.append(hwnd)
    return True

def readconfig():
    f = open('config', 'r')
    myconfig = {}
    for line in f:
        kvs = line.split("=")
        key = kvs[0]
        value = kvs[1]
        myconfig[key] = value
    f.close()
    global  classname,keys
    classname=myconfig["classname"].strip("\n")
    keys=myconfig["keys"]
def whileloop():
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    #hwnds = win32gui.FindWindow("notepad", None)
    #win32gui.SendMessage(hWnd,WM_CHAR,'c',0)
    while True:
        for hwid in hwnds:
            print(hwid)
            time.sleep(1)
            win32gui.SetForegroundWindow(hwid)
            time.sleep(1)
            for key in keys:
                keycode.key_input(key)
                time.sleep(0.3)
            time.sleep(1)
    print(hwnds)

def main():
    readconfig()
    whileloop()
if __name__ == "__main__":
   main()