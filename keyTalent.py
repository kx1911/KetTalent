import win32gui
import win32process
import win32api
import win32con
import time
import keycode
from tkinter import *  # 导入 Tkinter 库
from tkinter import ttk
import threading
import random

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
        #print(classid)
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
    keys = []
    global comboxlist,comboxlist2,comboxlist3
    keys.append(comboxlist.get())
    keys.append(comboxlist2.get())
    keys.append(comboxlist3.get())
    keys.append(comboxlist4.get())
    ptime = float(xtime.get())
    skilltime = float(xdelaytime.get())
    btnloop = xbts.get()
    print(comboxlist.get())
    # hwnds = win32gui.FindWindow("notepad", None)
    # win32gui.SendMessage(hWnd,WM_CHAR,'c',0)
    global flag
    print(keys)
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
                time.sleep(0.3 +  random.uniform(0, 0.1))
                win32gui.SetForegroundWindow(hwid)
                #keycode.mouse_rclick()
                time.sleep(0.3 +  random.uniform(0, 0.1))

                for key in keys:
                    print(btnloop)
                    if key == "鼠标左键":
                        time.sleep(0.1 + random.uniform(0, 0.3))
                        keycode.mouse_click()
                        continue
                    elif key == "鼠标右键":
                        time.sleep(0.1 + random.uniform(0, 0.3))
                        keycode.mouse_rclick()
                        continue
                    else:
                        time.sleep(skilltime + random.uniform(0, 0.3))
                        keycode.sendKey(keycode.VK_CODE[key])
                if len(btnloop) > 0:
                    for xbt in btnloop:
                        time.sleep(skilltime + random.uniform(0, 0.3))
                        keycode.sendKey(keycode.VK_CODE[xbt])
                time.sleep(ptime)
        # print(hwnds)

###TOdo :发送后台消息
def backgroundwhileloop():
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    keys = []
    global comboxlist,comboxlist2,comboxlist3
    keys.append(comboxlist.get())
    keys.append(comboxlist2.get())
    keys.append(comboxlist3.get())
    keys.append(comboxlist4.get())

    #print(comboxlist.get())
    # hwnds = win32gui.FindWindow("notepad", None)
    # win32gui.SendMessage(hWnd,WM_CHAR,'c',0)
    global flag
    #print(flag)
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
                #win32gui.SetForegroundWindow(hwid)
                #keycode.mouse_rclick()
                #time.sleep(1)

                for key in keys:
                    #print(key)
                    if key == "鼠标左键":
                        keycode.mouse_click()
                        break
                    elif key == "鼠标右键":
                        keycode.mouse_rclick()
                        break
                    else:
                        #print("send key " + key)
                        keycode.sendKeyback(hwid,keycode.VK_CODE[key])
                    time.sleep(0.3)
                time.sleep(1)
        # print(hwnds)

def startloop():
    global flag
    flag = True
    thread1 = threading.Thread(target=whileloop(), name='add')  # 线程对象.
    thread1.start()


def stoploog():
    global flag
    flag = False


def go(*args):
    # global  comboxlist
    print(comboxlist.get())  # 打印选中的值
    #print(comvalue)
def go2(*args):
    # global  comboxlist
    print(comboxlist2.get())  # 打印选中的值
    #print(comvalue)
def go3(*args):
    # global  comboxlist
    print(comboxlist3.get())  # 打印选中的值
    #print(comvalue)

def main():
    readconfig()
    # whileloop()
    Bu = Tk()
    Bu.title("KeyTalent")
    L1 = Label(Bu, text="按键1")
    L1.grid(row=0, column=0)
    comvalue1 = "鼠标";comvalue2 = "鼠标";comvalue3 = "鼠标"
    global comboxlist
    number = StringVar()
    comboxlist = ttk.Combobox(Bu, textvariable=number)  # 初始化
    keys = keycode.VK_CODE.keys()
    comboxlist["values"] = list(keys)
    comboxlist["state"] = "readonly"
    comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.grid(row=0, column=1)

    L2 = Label(Bu, text="按键2")
    L2.grid(row=1, column=0)
    global comboxlist2
    number2 = StringVar()
    comboxlist2 = ttk.Combobox(Bu, textvariable=number2)  # 初始化
    comboxlist2["values"] = list(keys)
    comboxlist2["state"] = "readonly"
    comboxlist2.current(28)  # 选择第一个
    comboxlist2.bind("<<ComboboxSelected>>", go2)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist2.grid(row=1, column=1)

    L3 = Label(Bu, text="按键3")
    L3.grid(row=2, column=0)
    global comboxlist3
    number3 = StringVar()
    comboxlist3 = ttk.Combobox(Bu, textvariable=number3)  # 初始化
    comboxlist3["values"] = list(keys)
    comboxlist3["state"] = "readonly"
    comboxlist3.current(28)  # 选择第一个
    comboxlist3.bind("<<ComboboxSelected>>", go3)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist3.grid(row=2, column=1)

    L4 = Label(Bu, text="按键4")
    L4.grid(row=3, column=0)
    global comboxlist4
    number4 = StringVar()
    comboxlist4 = ttk.Combobox(Bu, textvariable=number4)  # 初始化
    comboxlist4["values"] = list(keys)
    comboxlist4["state"] = "readonly"
    comboxlist4.current(28)  # 选择第一个
    comboxlist4.bind("<<ComboboxSelected>>", go3)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist4.grid(row=3, column=1)

    lbtns = Label(Bu, text='循环按键')
    lbtns.grid(row=4, sticky=W)
    global xbts
    xbts = Entry(Bu)
    xbts.grid(row=4, column=1, sticky=E)

    #print(comboxlist.get)
    l_user = Label(Bu, text='窗口间隔时间')
    l_user.grid(row=5, sticky=W)
    global xtime

    e = StringVar()
    xtime = Entry(Bu,textvariable=e)
    e.set("0")
    xtime.grid(row=5, column=1, sticky=E)

    # print(comboxlist.get)
    ldelay = Label(Bu, text='技能间隔时间')
    ldelay.grid(row=6, sticky=W)
    global xdelaytime
    f = StringVar()
    xdelaytime = Entry(Bu,textvariable=f)
    f.set("0")
    xdelaytime.grid(row=6, column=1, sticky=E)

    # E1 = Entry(Bu, bd=5)
    # E1.grid(row=0,column=2)
    Button(Bu, text=startcaption, anchor='c', fg='red', relief='ridge', compound='bottom', command=startloop)\
        .grid(row=7, column=0)
    Button(Bu, text=stopcaption, anchor='c', fg='red', relief='ridge', compound='bottom', command=stoploog)\
        .grid(row=7, column=1)
    Bu.mainloop()

if __name__ == "__main__":
    main()
