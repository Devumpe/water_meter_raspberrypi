import time
import RPi.GPIO as GPIO
import MFRC522
from threading import Thread
from Tkinter import *
import io
import sys
from subprocess import Popen
from datetime import *


RQS_0=0
RQS_QUIT=1
RQS_CAPTURE=2
rqs=RQS_0

root = Tk()
GPIO.setwarnings(False)
MIFAREReader = MFRC522.MFRC522()
HEIGHT = 1000
WIDTH = 1900
canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()

labeltexttop = Label(canvas,text="RFID", font='Helvetica 18 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.25,anchor='n')


def rfidHandler():
  global rqs
  rqs = RQS_0
  today = datetime.now()
  date = today.strftime('%d/%m/%Y:%H/%M/%S')
  
  textlabel.config(text="welcome")

  
  text_file = open('/home/pi/water-meter/data_for_show.txt','w')

  while rqs != RQS_QUIT:
    # Scan for cards
      (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
     
        # Get the UID of the card
      (status,uid) = MIFAREReader.MFRC522_Anticoll()
      
      if status == MIFAREReader.MI_OK:
     
         x=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
         rqs=RQS_QUIT
         

  textlabel.config(text=x,font=40)
  text_file.write(date+'\n')
  text_file.write(x+'\n')
  text_file.close()  

  

def startRfid():
    rfidThread = Thread(target=rfidHandler)
    rfidThread.start()
  
def linkcamera():
    import os
    Popen(["python" , "guiCamera.py"])

    global root
    root.destroy()


lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.15, anchor='n')

textlabel = Label(lower_frame,foreground='DeepSkyblue1')
textlabel.pack(side="bottom",fill="both",expand="yes")

button = Button(root,text="Next", font=40 ,command = linkcamera, background='DeepSkyblue3',foreground='white')
button.place(relx=0.3, rely=0.6, relheight=0.3, relwidth=0.4)

startRfid()
root.mainloop()

