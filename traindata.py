from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x730+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"img\h1.jpg")
        img=img.resize((1600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        lblone=Label(self.root,image=self.photoimg)
        lblone.place(x=0,y=0,width=1600,height=130)

        lbltitle=Label(lblone,text="TRAIN PHOTOS DATA", font=('Calibri',35,'bold'), bg='antique white',fg='black')
        lbltitle.place(x=70,y=30,width=1200,height=70)


        # #Code for Background Image
        bg_img=Image.open(r"img\bg1.jpg")
        bg_img=bg_img.resize((1600,720))
        self.photobgimg=ImageTk.PhotoImage(bg_img)
        bglbl=Label(self.root,image=self.photobgimg)
        bglbl.place(x=0,y=130,width=1600,height=720)

        trainherebtn=Button(bglbl,text="Click Here to Train Photos",command=self.train_photos,cursor="hand2",font=('Calibri',12,'bold'), bg='antique white',fg='black')
        trainherebtn.place(x=500,y=200,width=300,height=80)



        #function to train dataset
    def train_photos(self):
        data_dir=("imgdata")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        photoid=[]

        for image in path:
            img=Image.open(image).convert('L') #to convert picture to grayscale
            imgnp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imgnp)
            photoid.append(id)
            cv2.imshow("Training Photo",imgnp)
            cv2.waitKey(1)==13
        photoid=np.array(photoid)

        #Train classifier using LBPH algorithm
        clfr=cv2.face.LBPHFaceRecognizer_create()
        clfr.train(faces,photoid)
        clfr.write("trained_classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training Data process sucessfullyy completed")


if __name__ == "__main__":
    
    root =Tk()
    obj = train(root)
    root.mainloop()