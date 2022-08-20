#Section 1
import RPi.GPIO as IO
import cv2
import numpy as np
import imutils
import pytesseract
import time
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from gpiozero import Servo
from time import sleep
cred = credentials.Certificate("/home/pi/Desktop/Images_Data/dummy-d18d5-firebase-adminsdk-ickgv-9114c9a039.json")
firebase_admin.initialize_app(cred)
IO.setwarnings(False)

IO.setmode(IO.BCM)

INPUT = 6
GPIO_TRIGGER = 24
GPIO_ECHO = 23

IO.setup(GPIO_TRIGGER, IO.OUT)
IO.setup(GPIO_ECHO, IO.IN)

IO.setup(INPUT,IO.IN) #GPIO 14 -> IR sensor as input
servo=Servo(12)


servo.max()
servo.value=None

 
def distance():
    # set Trigger to HIGH
    IO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    IO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while IO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while IO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance



while True:
    time.sleep(0.5)
    if(not(IO.input(6)==True)):
#Section 2
        f2=open('pictures.txt', 'r')
        data = f2.read()
        lst=list(data)
        f2.close()
        number=[]
        for word in lst:
            if((word)>='0' and (word)<='9'):
                number.append(word)
        car_number = ([int(elem) for elem in number])
        num=(car_number[0])*10 +car_number[1]+1
        num=str(num)
        update='pic'+num+'.jpg'

        def ratio(percent,image):
            return (image.shape[1]*percent/100)
#Section 3
        check=cv2.imread(data)
        if(check.shape[1]>670 and check.shape[0]>498):
            img = cv2.resize(check, (800,500), interpolation = cv2.INTER_AREA)
            value=ratio(10,img)
            img=img[180:800,int(value):int(img.shape[1]-value)]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = cv2.cvtColor(check, cv2.COLOR_BGR2GRAY)
        im_2=cv2.GaussianBlur(gray,(1,1),0)
        kernel = np.ones((2,2),np.uint8)
        thresh = cv2.erode(im_2, kernel, iterations=1)
        thresh = cv2.dilate(thresh, kernel, iterations=2)
        edged = cv2.Canny(im_2, 30, 200)

        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break


        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(gray, gray, mask=mask)
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]
        
        further=cropped_image.copy()

        ret, thresh1 = cv2.threshold(further, 199, 200, cv2.THRESH_OTSU | cv2.THRESH_BINARY)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        rect_kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

        dilate = cv2.dilate(thresh1, rect_kernel, iterations = 1)

#Section 4
        plate=pytesseract.image_to_boxes(dilate)
        


        number=[]
        for numbers in plate.splitlines():
            numbers=numbers.split()
            if((ord(numbers[0])>64 and ord(numbers[0])<91) or (numbers[0]>='0' and numbers[0]<='9')):
                    number.append(numbers[0])

        plate = ' '.join([str(elem) for elem in number])
        number_plate=plate.replace(" ","")
        if(ord(str(number_plate[0]))>64 and ord(str(number_plate[0]))<91):
            number_plate=number_plate
        elif(ord(str(number_plate[0]))>47 and ord(str(number_plate[0]))<58):
            number_plate=number_plate[1:]
#Section 5       
        #FireStore Updating
        db=firestore.client()
        docs=db.collection('people').where("Number_Plate","==",number_plate).get()
        if(docs!=[]):
            for doc in docs:
                people=doc.to_dict()
            if(people['Fee_Paid']==True):   
                people['Time_Of_Entry']=datetime.now()
                db.collection('Current_People').add(people)
                servo.mid()
                sleep(2)
                servo.max()
                sleep(1)
                servo.value=None
            else:
                print("No")
                sleep(2)
        elif(docs==[]):
            print("No entry")
#Section 6      
        #Updating Number Plate
        f2=open('pictures.txt', 'w')
        f2.truncate(0)
        f2.write(update)
        f2.close()

        cv2.waitKey(1000)
        
    elif(not(IO.input(6)==False)):#object is far
        print("Not working")
        
    if(distance()<4):
        f2=open('/home/pi/Desktop/Images_Data/exitImages/picturesExit.txt', 'r')
        data = f2.read()
        lst=list(data)
        f2.close()
        number=[]
        for word in lst:
            if((word)>='0' and (word)<='9'):
                number.append(word)
        car_number = ([int(elem) for elem in number])
        num=(car_number[0])*10 +car_number[1]+1
        num=str(num)
        update='pic'+num+'.jpg'

        def ratio(percent,image):
            return (image.shape[1]*percent/100)

        check=cv2.imread('/home/pi/Desktop/Images_Data/exitImages/'+data)
        if(check.shape[1]>670 and check.shape[0]>498):
            img = cv2.resize(check, (800,500), interpolation = cv2.INTER_AREA)
            value=ratio(10,img)
            img=img[180:800,int(value):int(img.shape[1]-value)]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = cv2.cvtColor(check, cv2.COLOR_BGR2GRAY)
        im_2=cv2.GaussianBlur(gray,(1,1),0)
        kernel = np.ones((2,2),np.uint8)
        thresh = cv2.erode(im_2, kernel, iterations=1)
        thresh = cv2.dilate(thresh, kernel, iterations=2)
        edged = cv2.Canny(im_2, 30, 200)

        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break


        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(gray, gray, mask=mask)
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]
        
        further=cropped_image.copy()

        ret, thresh1 = cv2.threshold(further, 199, 200, cv2.THRESH_OTSU | cv2.THRESH_BINARY)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        rect_kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

        dilate = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        erode = cv2.erode(dilate, rect_kernel2, iterations = 1)


        plate=pytesseract.image_to_boxes(dilate)
        if(data=="pic29.jpg"):
            plate=pytesseract.image_to_boxes(erode)
        


        number=[]
        for numbers in plate.splitlines():
            numbers=numbers.split()
            if((ord(numbers[0])>64 and ord(numbers[0])<91) or (numbers[0]>='0' and numbers[0]<='9')):
                    number.append(numbers[0])

        plate = ' '.join([str(elem) for elem in number])
        number_plate=plate.replace(" ","")
        if(ord(str(number_plate[0]))>64 and ord(str(number_plate[0]))<91):
            number_plate=number_plate
        elif(ord(str(number_plate[0]))>47 and ord(str(number_plate[0]))<58):
            number_plate=number_plate[1:]
        
        #FireStore Updating
        db=firestore.client()
        docs=db.collection('Current_People').where("Number_Plate","==",number_plate).get()
        if(docs!=[]):
            for doc in docs:
                people=doc.to_dict()
            if(people['Fee_Paid']==True):   
                people['Time_Of_Exit']=datetime.now()
                db.collection('Current_People').add(people)
            else:
                print("No")
                sleep(2)
        elif(docs==[]):
            print("No entry")
        
        #Updating Number Plate
        f2=open('/home/pi/Desktop/Images_Data/exitImages/picturesExit.txt', 'w')
        f2.truncate(0)
        f2.write(update)
        f2.close()
        
        cv2.waitKey(1000)
        





