import cv2
import os
import numpy as np
#This module resizes image from a given directory to 100*100 pixels and writes all images to given directory
args = {
          'resizedOutput':r'E:\github\AI-Project\Digital Attendance System\resizedTrainingImages'
       }    
count=0
for path, subdirnames, filenames in os.walk("trainingImages"):
    for filename in filenames:
      if filename.startswith("."):
        print("Skipping File:",filename)#Skipping files that startwith .
        continue
      img_path=os.path.join(path, filename)#fetching image path
      print("img_path: ",img_path)
      id=os.path.basename(path)#fetching subdirectory names
      img = cv2.imread(img_path)
      if img is None:
        print("Image not loaded properly")
        continue
      resized_image = cv2.resize(img, (100, 100))
      # new_path="resizedTrainingImages"+"/"+str(id)

      new_path=args['resizedOutput']+"\\"+str(id)
      print(new_path)
      try:
        if not os.path.exists(new_path):
          os.makedirs(new_path)   
      except OSError: 
        print ('Error: Creating directory of data')

      print("desired path is: ",os.path.join(new_path, "frame%d.jpg" % count))#write all images to resizedTrainingImages/id directory
      
      # cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count),resized_image)

      new_path=new_path+"\\" +str(count) + ".jpg"
      cv2.imwrite(new_path, resized_image)
      count += 1