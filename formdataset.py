import cv2
import numpy as np
import os

facecascade=cv2.CascadeClassifier('face.xml')
print("Enter the Name of the Subject")
name=input()
if not os.path.exists(name):
	os.makedirs(name)


def captureface(x):
	d=0
	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
	for i in range(x+2) :
		ret,img=cap.read()
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces=facecascade.detectMultiScale(gray,1.3,5)
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
			filename = name+"/%d.png"%d
			if d<x:
				cv2.imwrite(filename,img[y:y+h,x:x+w])
			d+=1

		cv2.namedWindow('img')
		cv2.moveWindow('img', 40,30)
		cv2.imshow('img',img)
		k=cv2.waitKey(100)
		if k==100:
			break
		print(d)
	cap.release()
	cv2.destroyAllWindows()
#Front
captureface(40)
