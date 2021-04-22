from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class facialrecognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x730+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"img\h1.jpg")
        img=img.resize((1600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        lblone=Label(self.root,image=self.photoimg)
        lblone.place(x=0,y=0,width=1600,height=130)

        lbltitle=Label(lblone,text="FACE RECOGNITION WINDOW", font=('Calibri',35,'bold'), bg='antique white',fg='black')
        lbltitle.place(x=70,y=30,width=1200,height=70)


        # #Code for Background Image
        bg_img=Image.open(r"img\bg2.jpg")
        bg_img=bg_img.resize((1600,720))
        self.photobgimg=ImageTk.PhotoImage(bg_img)
        bglbl=Label(self.root,image=self.photobgimg)
        bglbl.place(x=0,y=130,width=1600,height=720)

        facebtn=Button(bglbl,text="Click here For Face Recognition",command=self.recog,cursor="hand2",font=('Calibri',16,'bold'), bg='antique white',fg='black')
        facebtn.place(x=500,y=230,width=400,height=120)

    #Function for Attendance
    def attend(self,fetchnm,fetchid,fetchcourse,fetchsem):
        with open("attend_file.csv","r+",newline="\n") as f:
            mydatalist = f.readlines()
            namelist=[]

            for line in mydatalist:
                d_entry=line.split((","))
                namelist.append(d_entry[0])
            if((fetchnm not in namelist) and (fetchid not in namelist) and (fetchcourse not in namelist) and (fetchsem not in namelist)):
                now=datetime.now()
                dt=now.strftime("%d/%m/%Y")
                stringdt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{fetchnm},{fetchid},{fetchcourse},{fetchsem},{stringdt},{dt},Present")

    #Main Face Recognition System Code
    def recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clfr):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)


            cordinates=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img , (x,y),(x+w,y+h),(255,0,255),3)
                id,predict=clfr.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host='localhost',username='root',password='Root@12345678',database='facerecognition')
                mycursor=conn.cursor()

                mycursor.execute("select Name from student where Student_ID="+str(id))
                fetchnm=mycursor.fetchone()
                fetchnm="+".join(fetchnm)

                mycursor.execute("select Course from student where Student_ID="+str(id))
                fetchcourse=mycursor.fetchone()
                fetchcourse="+".join(fetchcourse)

                mycursor.execute("select Semseter from student where Student_ID="+str(id))
                fetchsem=mycursor.fetchone()
                fetchsem="+".join(fetchsem)

                mycursor.execute("select Student_ID from student where Student_ID="+str(id))
                fetchid=mycursor.fetchone()
                fetchid="+".join(fetchid)

                if confidence>75:
                    cv2.putText(img,f"Name:{fetchnm}",(x,y-55),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255,3))
                    cv2.putText(img,f"Name:{fetchid}",(x,y-40),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255,3))
                    cv2.putText(img,f"Course:{fetchcourse}",(x,y-25),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255,3))
                    cv2.putText(img,f"Semester:{fetchsem}",(x,y-10),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255,3))
                    self.attend(fetchnm,fetchid,fetchcourse,fetchsem)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
                    cv2.putText(img,"Not Identified",(x,y-30),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255,3))

                cordinates=[x,y,w,h]
            return cordinates

        def recognize(img,clfr,faceCas):
            cordinates=draw_boundary(img,faceCas,1.1,10,(255,25,255),"Face",clfr)
            return img

        faceCas=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clfr=cv2.face.LBPHFaceRecognizer_create()
        clfr.read("trained_classifier.xml")

        photocap=cv2.VideoCapture(0)
        while True:
            ret,img=photocap.read()
            img=recognize(img,clfr,faceCas)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        photocap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    
    root =Tk()
    obj = facialrecognition(root)
    root.mainloop()