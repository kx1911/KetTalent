import win32gui
import win32process
import win32api
import win32con
import time
import keycode
from tkinter import *  # 导入 Tkinter 库
from tkinter import ttk
import threading

classname = "Notepad"
keys = 123
flag = False
startcaption = "START"
stopcaption = "STOP"
caption = startcaption
VKCODE = {}
flag1 = False
flag2 = False
flag3 = False


# 获取句柄
def callback(hwnd, hwnds):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        classid = win32gui.GetClassName(hwnd)
        print(classid)
        if classid == classname:
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
    global classname, keys
    classname = myconfig["classname"].strip("\n")
    keys = myconfig["keys"]


def whileloop():
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)

    # hwnds = win32gui.FindWindow("notepad", None)
    # win32gui.SendMessage(hWnd,WM_CHAR,'c',0)
    global flag
    print(flag)
    if flag:
        global caption
        caption = stopcaption
        while True:
            if flag == False:
                print("程序已停止")
                break
            for hwid in hwnds:
                if flag == False:
                    print("正在停止当前窗口")
                    break
                # print(hwid)
                time.sleep(1)
                win32gui.SetForegroundWindow(hwid)
                keycode.mouse_rclick()
                time.sleep(1)
                for key in keys:
                    keycode.key_input(key)
                    time.sleep(0.3)
                time.sleep(1)
        # print(hwnds)


def startloop():
    global flag
    flag = not flag
    thread1 = threading.Thread(target=whileloop, name='add')  # 线程对象.
    thread1.start()


def stoploog():
    global flag
    flag = False


def go(*args):
    # global  comboxlist
    #print(comboxlist.get())  # 打印选中的值
    print(comvalue)

def click_2():
    global flag2
    flag1 = not flag2


def main():
    readconfig()
    # whileloop()
    Bu = Tk()
    Bu.title("KeyTalent")
    L1 = Label(Bu, text="鼠标按键")
    L1.grid(row=0, column=0)
    comvalue = "鼠标"
    comboxlist = ttk.Combobox(Bu, textvariable=comvalue)  # 初始化
    comboxlist["values"] = ("鼠标左键", "鼠标右键")
    comboxlist["state"] = "readonly"
    comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.grid(row=0, column=1)
    print(comboxlist.get)
    # E1 = Entry(Bu, bd=5)
    # E1.grid(row=0,column=2)
    Button(Bu, text=startcaption, anchor='c', fg='red', relief='ridge', compound='bottom', command=startloop)\
        .grid(row=2, column=0)
    Button(Bu, text=stopcaption, anchor='c', fg='red', relief='ridge', compound='bottom', command=stoploog)\
        .grid(row=2, column=1)
    Bu.mainloop()

if __name__ == "__main__":
    main()
