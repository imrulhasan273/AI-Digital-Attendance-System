import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import os
from imutils import paths
import glob

args = {
          'input':r'E:\github\AI-Project\Digital Attendance System\draftImages',
          'output':r'E:\github\AI-Project\Digital Attendance System\trainingImages'
       }

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Digital Attendance System")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1000x500')

'''
window.configure(background='gray')
'''
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Digital Attendance System"  ,fg="black"  ,width=45  ,height=1,font=('times', 30, 'bold underline')) 
message.place(x=0, y=0)

lbl = tk.Label(window, text="Registration",width=40  ,height=1  ,fg="blue"  ,font=('times', 15, ' bold ') ) 
lbl.place(x=0, y=50)

lbl = tk.Label(window, text="Attendance",width=40  ,height=1  ,fg="blue"  ,font=('times', 15, ' bold ') ) 
lbl.place(x=380, y=50)

#____________ID______________
lbl = tk.Label(window, text="Enter Your ID",width=10  ,height=8  ,fg="black"  ,font=('times', 15, ' bold ') ) 
lbl.place(x=17, y=50)
txt = tk.Entry(window,width=20,fg="black",font=('times', 15, ' normal '))
txt.place(x=203, y=130)
#_____________Name_____________
lbl2 = tk.Label(window, text="Enter Your Name",width=15  ,fg="black",height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=0, y=170)
txt2 = tk.Entry(window,width=20   ,fg="black",font=('times', 15, ' normal ')  )
txt2.place(x=200, y=180)
#____________________Button to input video sequence ( videotoimage.py )
def vedeoToImg():
    os.system('python videotoimg.py')
startBrowse = tk.Button(window, text="StartRecording", command=vedeoToImg  ,fg="#0029b3"   ,width=10  ,height=1, activebackground = "green" ,font=('times', 15, ' bold '))
startBrowse.place(x=20, y=240)

#____________________Button to move video sequence to trainingimages folder (Save Button)
def moveToTrainImages():
    Id=(txt.get())
    name=(txt2.get())
    print("ID: ",Id)
    print("Name: ",name)
    imagePaths = list(paths.list_images(args["input"]))
    print(imagePaths) #all the images path are here....

    args['output'] = args["output"] +"\\" + str(Id)
    print(args['input'])
    print(args['output'])
    try:      
        if not os.path.exists(args['output']): 
            os.makedirs(args['output'])   
    except OSError: 
        print ('Error: Creating directory of data')
    cnt=0
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        # cv2.imshow(image)
        cnt=cnt+1
        p=args['output']+"\\" +str(cnt) + ".jpg"
        cv2.imwrite(p, image)
    RemoveFiles = args['input'] + "\\" + "*"
    files = glob.glob(RemoveFiles)

    for f in files:
        os.remove(f)
    #__create dict____
    row = [Id , name]
    with open('EmployeeDetails/EmployeeDetails.csv','a+', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    os.system('python resizeImages.py')
    os.system('python tester.py')
startBrowse = tk.Button(window, text="Save", command=moveToTrainImages  ,fg="green"   ,width=10  ,height=1, activebackground = "green" ,font=('times', 15, ' bold '))
startBrowse.place(x=180, y=240)


#_______________________Button to Recognize an employee _____________________
def recognizeEmp():
    os.system('python videoTester.py')
startBrowse = tk.Button(window, text="Mark My Attendance", command=recognizeEmp  ,fg="black"   ,width=15  ,height=1, activebackground = "green" ,font=('times', 15, ' bold '))
startBrowse.place(x=490, y=150)


#---------------------------NOTIFICATION ---------------------------------------------------
lbl3 = tk.Label(window, text="Attendance : ",width=10  ,fg="black"   ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=480, y=400)
message2 = tk.Label(window, text="Successfull" ,fg="green"  ,activeforeground = "green",width=15  ,height=2  ,font=('times', 15, ' normal ')) 
message2.place(x=590, y=400)

lbl3 = tk.Label(window, text="Notification : ",width=10  ,fg="black"   ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=20, y=400)
message2 = tk.Label(window, text="some action" ,fg="green"  ,activeforeground = "green",width=15  ,height=2  ,font=('times', 15, ' normal ')) 
message2.place(x=200, y=400)
#-------------------------------------------------------------------------------


#______________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=100)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=120)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=140)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=160)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=180)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=200)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=220)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=240)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=260)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=280)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=300)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=320)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=340)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=360)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=380)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=400)
lbl3 = tk.Label(window, text="|",width=1  ,fg="black"   ,height=0 ,font=('times', 15, ' bold')) 
lbl3.place(x=420, y=420)
#_______________________________________________________________________________________________________



quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"    ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=890, y=410)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 20, 'italic'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Developed by Imrul")
copyWrite.configure(state="disabled",fg="blue"  )
copyWrite.pack(side="left")
copyWrite.place(x=20, y=450)
 
window.mainloop()