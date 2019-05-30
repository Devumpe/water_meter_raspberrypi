#-*- coding: utf-8 -*-
from google.cloud import storage
import pyrebase
import time
from tkinter import *
from PIL import ImageTk, Image
from subprocess import Popen
import os
import urllib2
from threading import Thread

def readFile():
    global root
    root = Tk()
    
    canv = Canvas(root, width=1900, height=1000, bg='white')
    canv.grid(row=2, column=3)
    labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 35 bold',background='DeepSkyblue2',foreground='white')
    labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.2,anchor='n')

    
    photo = Image.open("correct.jpg")

    photo.resize((5, 5), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(photo)  
    background_label = Label(root,background='white', image=img)
    background_label.place(relx=0.5, rely=0.25,relwidth=0.4, relheight=0.4,anchor='n')



    
    textlabel = Label(root,background='white',foreground='DeepSkyblue3',text='Upload Done!',font='Helvetica 22 bold')
    textlabel.place(relx=0.5, rely=0.75,anchor='n')

   
    button = Button(root,text="NEXT", font='Helvetica 30' , background='DeepSkyblue3',foreground='white',command=linklogin)
    button.place(relx=0.3, rely=0.83, relheight=0.15, relwidth=0.4)




    root.mainloop()
    text_file = open('data_for_upload.txt','r')
    line = text_file.read().splitlines()
    #print (len(line))
    for i in range(0,len(line)):  
        if(i%4==0):
            textuser = line[i]
            textrfid = line[i+1]
            textdate = line[i+2]
            textimage = line[i+3]  
            upimage( textuser, textrfid , textdate,textimage)
            #return (textdate , textrfid , textimage)

def internet_on():
    global root

    try:
        urllib2.urlopen('http://www.google.com/')

        #Popen(["python", "upimage.py"])
        readFile()

    except urllib2.URLError as err:
        print ("Please check your internet.")
        root = Tk()
    
        canv = Canvas(root, width=1900, height=1000, bg='white')
        canv.grid(row=2, column=3)
        labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 35 bold',background='DeepSkyblue2',foreground='white')
        labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.2,anchor='n')

        
        photo = Image.open("incorrect.png")

        photo.resize((5, 5), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(photo)  
        background_label = Label(root,background='white', image=img)
        background_label.place(relx=0.5, rely=0.25,relwidth=0.4, relheight=0.4,anchor='n')



        
        textlabel = Label(root,background='white',foreground='red',text='Upload Fail!',font='Helvetica 22 bold')
        textlabel.place(relx=0.5, rely=0.75,anchor='n')

       
        button = Button(root,text="NEXT", font='Helvetica 30' , background='DeepSkyblue3',foreground='white',command=linklogin)
        button.place(relx=0.3, rely=0.83, relheight=0.15, relwidth=0.4)




        root.mainloop()

def linklogin():
    Popen(["python" , "login.py"])

    global root
    root.destroy()


def upimage(user,rfid,date,image):
# ไฟล์ที่จะอัw
    
    config = {
    "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
    "authDomain": "water-meter-235712.firebaseapp.com",
    "databaseURL": "https://water-meter-235712.firebaseio.com",
    "projectId": "water-meter-235712",
    "storageBucket": "water-meter-235712.appspot.com",
    "messagingSenderId": "67042893322"   
    }
    # data = readFile()
    # date = data[0]
    # rfid = data[1]
    # image = data[2]

    filename = image

    credential_path = "/home/pi/water-meter/water-meter-235712-firebase-adminsdk-ebgws-8362ef71ab.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    # ที่อยู่ bucket
    client = storage.Client()
    bucket = client.get_bucket('water-meter-235712.appspot.com')

    # อัพไฟล์ storage
    blob = bucket.blob(image)
    with open(filename, "rb") as fp:
        blob.upload_from_file(fp)
    print(blob.public_url)

    #อัพไฟล์ database
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

    db.child("room").push({"image": {"staffname":user,"rfid":rfid,"date": date,"url": blob.public_url}})
    open("data_for_upload.txt", 'w').close()






if __name__ == "__main__":
    
   internet_on()



