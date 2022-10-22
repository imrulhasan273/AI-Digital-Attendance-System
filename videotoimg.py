import cv2
cap=cv2.VideoCapture(0)
count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
    count += 1
    cv2.imwrite("draftImages/frame%d.jpg" % count, test_img)     # save frame as JPG file
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    if(count==500):
        break
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break
cap.release()
cv2.destroyAllWindows


# #__________________________________________________________________________________
# import cv2
# from imutils import paths
# cam = cv2.VideoCapture(0)
# harcascadePath = "HaarCascade/haarcascade_frontalface_default.xml"
# detector=cv2.CascadeClassifier(harcascadePath)
# sampleNum=0
# while(True):
#     ret, img = cam.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = detector.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
#         sampleNum=sampleNum+1
#         cv2.imwrite("draftImages/frame%d.jpg" % sampleNum, gray[y:y+h,x:x+w]) 
#         cv2.imshow('frame',img)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#     elif sampleNum>60:
#         break
# cam.release()
# cv2.destroyAllWindows() 