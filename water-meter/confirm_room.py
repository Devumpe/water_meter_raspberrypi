
from Tkinter import *
from functools import partial
import time
from threading import Thread
import io
import sys
from subprocess import Popen
from datetime import *
import os

def click(btn):
    global pin
  
    if btn == 'Del':
        pin = pin[:-1]
        textentry.delete('0','end')
        textentry.insert('end',pin)

    
    elif btn == 'Enter':
        if btn == ' ':
            print('please type username')
        else:
            textentry.insert('end',pin)
            linkcamera()
        
    else:
        pin += btn
        textentry.insert('end', btn)
    
def linkcamera():
    today = datetime.now()
    date = today.strftime('%d/%m/%Y Time = %H:%M:%S')
    text_file = open('data_for_show.txt','a')
    text_file.write(pin+'\n')
    text_file.write(date+'\n')
    text_file.close()
    Popen(["python" , "guiCamera.py"])

    global boot
    boot.destroy()

boot = Tk()
boot['bg'] = 'white'
boot.geometry("1900x1000")

labeltexttop = Label(boot,text="RFID", font='Helvetica 18 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.1,anchor='n')


lower_frame = Frame(boot, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.26, anchor='n')


#textlabel = Label(lower_frame,font='Helvetica 22',foreground='DeepSkyblue1')
#textlabel.pack(side="bottom",fill="both",expand="yes")
textentry = Entry(lower_frame,font='Helvetica 45 bold',foreground='DeepSkyblue2')
textentry.pack(side="bottom",fill="both",expand="yes")

lf = LabelFrame(boot, text=" keypad ", bd=15)
lf.place(relx=0.01, rely=0.35, relheight=1, relwidth=1)

btn_list = [
    '7',  '8',  '9',
    '4',  '5',  '6',
    '1',  '2',  '3',
    '0',  'Del','Enter']

pin = ''
r = 1
c = 0
n = 0

btn = list(range(len(btn_list)))
for label in btn_list:
    cmd = partial(click, label)
    btn[n] = Button(lf, text=label, width=19, height=2, command=cmd,font='Helvetica 30 bold')
    btn[n].grid(row=r, column=c)

    n += 1

    c += 1
    if c == 3:
        c = 0
        r += 1
boot.mainloop()
