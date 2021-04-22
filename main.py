from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from Student import student
from traindata import train
from facial import facialrecognition
from attendence import student_attend
import os

class FaceRecognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x730+0+0")
        self.root.title("Face Recognition System")
        #root.resizable(False, True)


        #Code for heading image
        img=Image.open(r"img\h1.jpg")
        img=img.resize((1600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        lblone=Label(self.root,image=self.photoimg)
        lblone.place(x=0,y=0,width=1600,height=130)

        def current_time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,current_time)
        lbl=Label(lblone,font=('Calibri',12,'bold'),bg='peach puff',fg='black')
        lbl.place(x=550,y=100,width=150,height=30)
        current_time()

        # #Code for Background Image
        bg_img=Image.open(r"img\bg1.jpg")
        bg_img=bg_img.resize((1600,720))
        self.photobgimg=ImageTk.PhotoImage(bg_img)
        bglbl=Label(self.root,image=self.photobgimg)
        bglbl.place(x=0,y=130,width=1600,height=720)


        # #code for heading of software
        lbltitle=Label(lblone,text="ADVANCED FACE RECOGNITION SYSTEM", font=('Calibri',35,'bold'), bg='antique white',fg='black')
        lbltitle.place(x=70,y=30,width=1200,height=70)

        # #code for student button
        stud_img=Image.open(r"img\student.png")
        stud_img=stud_img.resize((150,130))
        self.photostudimg=ImageTk.PhotoImage(stud_img)

        stud_btn=Button(bglbl,image=self.photostudimg,command=self.student_details,cursor="hand2")
        stud_btn.place(x=100,y=80,width=180,height=130)
        stud_btn_lbl=Button(bglbl,text="Get Student Details",command=self.student_details,cursor="hand2",font=('Calibri',12,'bold'), bg='antique white',fg='black')
        stud_btn_lbl.place(x=100,y=200,width=180,height=30)

        #button for detect image
        det_img=Image.open(r"img\detface.png")
        det_img=det_img.resize((150,130))
        self.photodetimg=ImageTk.PhotoImage(det_img)

        det_btn=Button(bglbl,image=self.photodetimg,cursor="hand2",command=self.face_recog)
        det_btn.place(x=100,y=300,width=180,height=130)
        det_btn_lbl=Button(bglbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=('Calibri',12,'bold'), bg='antique white',fg='black')
        det_btn_lbl.place(x=100,y=420,width=180,height=30)


        #Facial Attendance Button
        att_img=Image.open(r"img\att.png")
        att_img=att_img.resize((150,130))
        self.photoattimg=ImageTk.PhotoImage(att_img)

        att_btn=Button(bglbl,image=self.photoattimg,cursor="hand2",command=self.page_attend)
        att_btn.place(x=500,y=80,width=180,height=130)
        att_btn_lbl=Button(bglbl,text="Attendance Database",cursor="hand2",command=self.page_attend,font=('Calibri',12,'bold'), bg='antique white',fg='black')
        att_btn_lbl.place(x=500,y=200,width=180,height=30)


        #Training Face Data Button
        train_img=Image.open(r"img\train.png")
        train_img=train_img.resize((150,130))
        self.phototrainimg=ImageTk.PhotoImage(train_img)

        train_btn=Button(bglbl,image=self.phototrainimg,cursor="hand2",command=self.train_img)
        train_btn.place(x=500,y=300,width=180,height=130)
        train_btn_lbl=Button(bglbl,text="Train Data",cursor="hand2",command=self.train_img,font=('Calibri',12,'bold'), bg='antique white',fg='black')
        train_btn_lbl.place(x=500,y=420,width=180,height=30)


         #Photos data Button
        photodata_img=Image.open(r"img\photosdata.png")
        photodata_img=photodata_img.resize((150,130))
        self.photodataimg=ImageTk.PhotoImage(photodata_img)

        photodata_btn=Button(bglbl,image=self.photodataimg,cursor="hand2",command=self.opn_img)
        photodata_btn.place(x=900,y=80,width=160,height=130)
        photodata_btn_lbl=Button(bglbl,text="Photos Database",cursor="hand2",command=self.opn_img,font=('Calibri',12,'bold'), bg='antique white',fg='black')
        photodata_btn_lbl.place(x=900,y=200,width=160,height=30)

        #Need Help and Exit Button code
        help_img=Image.open(r"img\help.png")
        help_img=help_img.resize((150,130))
        self.help_img=ImageTk.PhotoImage(help_img)

        exit_img=Image.open(r"img\eit.jpg")
        exit_img=exit_img.resize((150,130))
        self.exit_img=ImageTk.PhotoImage(exit_img)

        help_btn=Button(bglbl,image=self.help_img,cursor="hand2",command=self.need_help)
        help_btn.place(x=900,y=300,width=150,height=100)
        help_btn_lbl=Button(bglbl,text="Need Help?",cursor="hand2",command=self.need_help,font=('Calibri',12,'bold'), bg='antique white',fg='black')
        help_btn_lbl.place(x=900,y=370,width=150,height=35)

        exit_btn_lbl=Button(bglbl,text="Close",cursor="hand2",command=self.exit_project,font=('Calibri',12,'bold'), bg='antique white',fg='black')
        exit_btn_lbl.place(x=900,y=410,width=150,height=40)



    def opn_img(self):
        os.startfile("imgdata")

    def need_help(self):
        messagebox.showinfo("Help","Stuck Somewhere??,\nMail us at: developer@project.com")
        
    def exit_project(self):
        self.exit_project=tkinter.messagebox.askyesno("Exit","Make Sure you have saved your data,\nyou want to exit?")
        if self.exit_project>0:
            self.root.destroy()
        else:
            return

        #Function to redirect to new windows
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.redirect=student(self.new_window)

    def train_img(self):
        self.new_window=Toplevel(self.root)
        self.redirect=train(self.new_window) 

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.redirect=facialrecognition(self.new_window) 

    def page_attend(self):
        self.new_window=Toplevel(self.root)
        self.redirect=student_attend(self.new_window)



if __name__ == "__main__":
    root =Tk()
    obj = FaceRecognition(root)
    root.mainloop()