
from Tkinter import *
from functools import partial
import time
from threading import Thread
import io
import sys
from subprocess import Popen
import os


def click(btn):
    global username

  
    if btn == 'Del':
        username = username[:-1]
        textentry.delete('0','end')
        textentry.insert('end',username)

    
    elif btn == 'Enter':
        if btn == '':
            print('please type username')
        else:
            textentry.insert('end',username)
            linkcomfirm()
    else:
        username += btn
    
        textentry.insert('end', btn)
    text_file = open('data_for_show.txt','w')
    text_file.write(username+'\n')
    text_file.close()
    
def linkcomfirm():
    Popen(["python" , "confirm_room.py"])

    global boot
    boot.destroy()

boot = Tk()
boot['bg'] = 'white'
boot.geometry("1900x1000")

labeltexttop = Label(boot,text="Login", font='Helvetica 15 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.1,anchor='n')


lower_frame = Frame(boot, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.26, anchor='n')


#textlabel = Label(lower_frame,font='Helvetica 22',foreground='DeepSkyblue1')
#textlabel.pack(side="bottom",fill="both",expand="yes")
textentry = Entry(lower_frame,font='Helvetica 45 bold',foreground='DeepSkyblue2')

textentry.pack(side="bottom",fill="both",expand="yes")

lf = LabelFrame(boot, text=" keypad ", bd=15)
lf.place(relx=0.01, rely=0.35, relheight=1, relwidth=1)

btn_list = ['q','w','e','r','t','y','u','i','o','p',
'a','s','d','f','g','h','j','k','l',
'z','x','c','v','b','n','m' ,'Del','Enter'   ]

username = ''
r = 1
c = 0
n = 0

btn = list(range(len(btn_list)))
for label in btn_list:
    cmd = partial(click, label)
    btn[n] = Button(lf, text=label, width=7, height=2, command=cmd,font='Helvetica 29 bold')
    btn[n].grid(row=r, column=c)

    n += 1

    c += 1
    if c == 7:
        c = 0
        r += 1
boot.mainloop()
