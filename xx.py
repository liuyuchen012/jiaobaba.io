from tkinter import *
from tkinter.messagebox import *
import os

def j():
    window = Tk()
    window.withdraw()  # 退出默认 tk 窗口

    result = showinfo('提示', '儿子/女儿真乖')
    print(f'提示: {result}')
    os._exit(0)
def bj():
    window = Tk()
    window.withdraw()  # 退出默认 tk 窗口

    result = showinfo('提示', '不叫爸爸休想关毕弹窗')
    print(f'提示: {result}')

while True:
    window = Tk()
    window.title("叫爸爸")
    window.geometry("500x100")
    lbl = Label(window, text="                 叫爸爸", font=("Arial Bold", 30))
    lbl.grid(column=0, row=0)

    btn = Button(window, text="爸爸", command=j)
    btn.grid(column=0, row=2)
    btn = Button(window, text="不叫", command=bj)
    btn.grid(column=2, row=2)
    window.mainloop()
