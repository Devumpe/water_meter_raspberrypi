from Tkinter import *
from PIL import Image,ImageTk
from subprocess import Popen

root = Tk()
text = Text(root)
HEIGHT = 1000
WIDTH = 1900
canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()



def linkdatabase():

    import os
    Popen(["python" , "upImage.py"])

    global root
    root.destroy()
    

labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 35 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.2,anchor='n')

i=0;
text_file = open('/home/pi/water-meter/data_for_show.txt','r')
mem_file = open('/home/pi/water-meter/data_for_memory.txt','a')
upload_file = open('/home/pi/water-meter/data_for_upload.txt','a')

line = text_file.read().splitlines()   
textusername = line[i]
textrfid = line[i+1]
textdate = line[i+2]
textimage = line[i+3]
mem_file.write(textusername+'\n'+textrfid+'\n'+textdate+'\n'+textimage+'\n')
upload_file.write(textusername+'\n'+textrfid+'\n'+textdate+'\n'+textimage+'\n') 
text_file.close()
mem_file.close()
upload_file.close()


photo = Image.open(textimage)
#photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
label = Label(root,image=img)
label.place(relx=0.3, rely=0.25,anchor='n')


userframe = Frame(root, bg='#80c1ff', bd=10)
userframe.place(relx=0.85, rely=0.25, relwidth=0.3, relheight=0.15, anchor='n')

userlabel = Label(userframe,foreground='DeepSkyblue3',text="Staffname = "+textusername,font='Helvetica 25 bold')
userlabel.pack(side="bottom",fill="both",expand="yes")


keyframe = Frame(root, bg='#80c1ff', bd=10)
keyframe.place(relx=0.85, rely=0.45, relwidth=0.3, relheight=0.15, anchor='n')

uidlabel = Label(keyframe,foreground='DeepSkyblue3',text="Key Room = "+textrfid,font='Helvetica 25 bold')
uidlabel.pack(side="bottom",fill="both",expand="yes")


dateframe = Frame(root, bg='#80c1ff', bd=10)
dateframe.place(relx=0.85, rely=0.65, relwidth=0.3, relheight=0.15, anchor='n')

timelabel = Label(dateframe,foreground='DeepSkyblue3',text="Date = "+textdate,font='Helvetica 15 bold')
timelabel.pack(side="bottom",fill="both",expand="yes")




summitbtn= Button( root,text="SUMMIT", font='Helvetica 30' , background='DeepSkyblue3',foreground='white', command=linkdatabase)
summitbtn.place(relx=0.7, rely=0.83, relheight=0.15, relwidth=0.4)




root.mainloop()
