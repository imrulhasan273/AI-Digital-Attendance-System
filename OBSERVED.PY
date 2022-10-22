# import csv
# reader = csv.reader(open('EmployeeDetails/EmployeeDetails.csv'))
# name = {}
# count=0
# for row in reader:
#     count+=1
#     if count==1:
#         continue
#     key = int(row[0])
#     if key in name:
#         # implement your duplicate row handling here
#         pass
#     name[key] = row[1]
# print(name)




# import os
# import cv2
# import numpy as np
# import faceRecognition as fr
# import csv

# #This module captures images via webcam and performs face recognition
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('trainingData.yml')#Load saved training data

# reader = csv.reader(open('EmployeeDetails/EmployeeDetails.csv'))
# name = {}
# m=0
# for row in reader:
#   m+=1
#   if m==1:
#     continue
#   key = int(row[0])
#   if key in name:
#       # implement your duplicate row handling here
#       pass
#   name[key] = row[1]
# # print(name)
# # name = {0 : "Priyanka",1 : "Kangana",16101034 : "Imrul"}
# cap=cv2.VideoCapture(0)
# while True:
#     ret,test_img=cap.read()# captures frame and returns boolean value and captured image
#     faces_detected,gray_img=fr.faceDetection(test_img)

#     for (x,y,w,h) in faces_detected:
#       cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

#     resized_img = cv2.resize(test_img, (1000, 700))
#     cv2.imshow('face detection Tutorial ',resized_img)
#     cv2.waitKey(10)

#     for face in faces_detected:
#         (x,y,w,h)=face
#         roi_gray=gray_img[y:y+w, x:x+h]
#         label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
#         print("confidence:",confidence)
#         print("label:",label)
#         fr.draw_rect(test_img,face)
#         predicted_name=name[label] + "HI"
#         if confidence > 39:#If confidence less than 37 then don't print predicted face text on screen
#            fr.put_text(test_img,predicted_name,x,y)

#     resized_img = cv2.resize(test_img, (1000, 700))
#     cv2.imshow('face recognition tutorial ',resized_img)
#     if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
#         break

# cap.release()
# cv2.destroyAllWindows


import os
import cv2
import numpy as np
import faceRecognition as fr
import csv
import tkinter as tk
from tkinter import Message ,Text
import shutil
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

idCOL=16101034
nameCOL="Hasan"

col_names =  ['Id','Name','Date','Time']
attendance = pd.DataFrame(columns = col_names)
# Pass the row elements as key value pairs to append() function 
ts = time.time()      
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
Hour,Minute,Second=timeStamp.split(":")

attendance = attendance.append({'Id' : idCOL , 'Name' : nameCOL, 'Date': date, 'Time': timeStamp} , ignore_index=True)     
fileName="Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
attendance.to_csv(fileName,index=False)