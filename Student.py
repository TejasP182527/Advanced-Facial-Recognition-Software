from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x730+0+0")
        self.root.title("Face Recognition System")
        #root.resizable(False, True)


        #Variables for Data 
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_course=StringVar()
        self.var_cyear=StringVar()
        self.var_ayear=StringVar()
        self.var_sem=StringVar()
        #self.var_photo=StringVar()
        
         #Code for heading image
        img=Image.open(r"img\h1.jpg")
        img=img.resize((1600,130))
        self.photoimg=ImageTk.PhotoImage(img)
        lblone=Label(self.root,image=self.photoimg)
        lblone.place(x=0,y=0,width=1600,height=130)
        lbltitle=Label(lblone,text="STUDENT DATABASE", font=('Calibri',35,'bold'), bg='antique white',fg='black')
        lbltitle.place(x=70,y=30,width=1200,height=70)


        # #Code for Background Image
        bg_img=Image.open(r"img\bg1.jpg")
        bg_img=bg_img.resize((1600,720))
        self.photobgimg=ImageTk.PhotoImage(bg_img)
        bgstudlbl=Label(self.root,image=self.photobgimg)
        bgstudlbl.place(x=0,y=130,width=1600,height=720)

        dbasewindow=Frame(bgstudlbl,bd=2,borderwidth=0)
        dbasewindow.place(x=5,y=5,width=1580,height=690)

        #to create frame within frame
        leftframe=LabelFrame(bgstudlbl,bd=2,relief=RIDGE,borderwidth=0)
        leftframe.place(x=5,y=5,width=650,height=720)

        studframe=LabelFrame(leftframe,bd=2,relief=RIDGE,borderwidth=0,text="Student Details",font=('Calibri',17,'bold'))
        studframe.place(x=5,y=5,width=630,height=200)

        studnm=Label(studframe,text="Name: ",font=('Calibri',12))
        studnm.grid(row=0,column=0)
        studnmtxt=ttk.Entry(studframe,textvariable=self.var_name,width=20,font=('Calibri',12))
        studnmtxt.grid(row=0,column=1,padx=10,sticky=W)

        studid=Label(studframe,text="Student ID: ",font=('Calibri',12))
        studid.grid(row=0,column=2,padx=10)
        studidtxt=ttk.Entry(studframe,textvariable=self.var_id,width=20,font=('Calibri',12))
        studidtxt.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        studmail=Label(studframe,text="Email ID: ",font=('Calibri',12))
        studmail.grid(row=1,column=0,padx=10,pady=15)
        studmailtxt=ttk.Entry(studframe,textvariable=self.var_email,width=20,font=('Calibri',12))
        studmailtxt.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        studphone=Label(studframe,text="Contact: ",font=('Calibri',12))
        studphone.grid(row=1,column=2,padx=10,pady=15)
        studphonetxt=ttk.Entry(studframe,textvariable=self.var_contact,width=20,font=('Calibri',12))
        studphonetxt.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        studadd=Label(studframe,text="Address: ",font=('Calibri',12))
        studadd.grid(row=2,column=0,padx=10,pady=15)
        studaddtxt=ttk.Entry(studframe,textvariable=self.var_address,width=20,font=('Calibri',12))
        studaddtxt.grid(row=2,column=1,padx=10,pady=15,sticky=W)

        studgen=Label(studframe,text="Gender: ",font=('Calibri',12))
        studgen.grid(row=2,column=2,padx=10,pady=15)
        studgentxt=ttk.Entry(studframe,textvariable=self.var_gender,width=20,font=('Calibri',12))
        studgentxt.grid(row=2,column=3,padx=3,pady=10,sticky=W)

        #course frame under left Frame
        courseframe=LabelFrame(leftframe,bd=2,relief=RIDGE,borderwidth=0,text="Course Information",font=('Calibri',17,'bold'))
        courseframe.place(x=5,y=210,width=640,height=280)

        #Course and Combobox
        dept_label=Label(courseframe,text="Course",font=('Calibri',12))
        dept_label.grid(row=0,column=0,padx=10,sticky=W)
        dept_courses=ttk.Combobox(courseframe,textvariable=self.var_course,font=('Calibri',12),state="readonly")
        dept_courses.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        dept_courses["values"]=("Select Course","BCA","MCA","MCS")
        dept_courses.current(0)

        #Academic Year
        ayear_label=Label(courseframe,text="Academic Year",font=('Calibri',12))
        ayear_label.grid(row=0,column=2,padx=10,sticky=W)
        ayear_year=ttk.Combobox(courseframe,textvariable=self.var_ayear,font=('Calibri',12),state="readonly")
        ayear_year.grid(row=0,column=3,padx=3,pady=10,sticky=W)
        ayear_year["values"]=("2020-21","2021-22")
        ayear_year.current(0)

        #Course Year
        course_year=Label(courseframe,text="Course Year",font=('Calibri',12))
        course_year.grid(row=2,column=0,padx=10,sticky=W)
        course_year=ttk.Combobox(courseframe,textvariable=self.var_cyear,font=('Calibri',12),state="readonly")
        course_year.grid(row=2,column=1,padx=3,pady=10,sticky=W)
        course_year["values"]=("F.Y","S.Y","T.Y")
        course_year.current(0)

        #Semester
        course_sem=Label(courseframe,text="Semester",font=('Calibri',12))
        course_sem.grid(row=2,column=2,padx=10,sticky=W)
        course_sem=ttk.Combobox(courseframe,textvariable=self.var_sem,font=('Calibri',12),state="readonly")
        course_sem.grid(row=2,column=3,padx=3,pady=10,sticky=W)
        course_sem["values"]=("I","II","III","IV","V","VI")
        course_sem.current(0)


        #Buttons to take photos
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(courseframe,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=3,column=0)

        #self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(courseframe,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=0,padx=3)

        #Extra Buttons Frane
        btnframe=Frame(courseframe,bd=2,relief=RIDGE,borderwidth=0)
        btnframe.place(x=5,y=150,width=610,height=40)

        btnsave=Button(btnframe,text="Save",command=self.add_data,width=17,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnsave.grid(row=0,column=0,padx=3)

        btnupdate=Button(btnframe,text="Update",command=self.update_data, width=17,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnupdate.grid(row=0,column=1,padx=3)

        btndel=Button(btnframe,text="Delete",command=self.delete_data, width=17,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btndel.grid(row=0,column=2,padx=3)

        btnreset=Button(btnframe,text="Reset", command=self.reset_form,width=17,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnreset.grid(row=0,column=3)

        #Click from Camera buttons
        btnframe1=Frame(courseframe,bd=2,relief=RIDGE,borderwidth=0)
        btnframe1.place(x=4,y=190,width=610,height=40)

        btnclick=Button(btnframe1,text="Take Photo",command=self.generate_data, width=37,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnclick.grid(row=0,column=0,padx=5)

        photoupdate=Button(btnframe1,text="Update Photo", width=35,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        photoupdate.grid(row=0,column=1)


        #Right Frame
        rightframe=LabelFrame(bgstudlbl,bd=2,relief=RIDGE,text="Search Student Details Here: ",borderwidth=0,font=('Calibri',15,'bold'))
        rightframe.place(x=665,y=5,width=700,height=720)

        #Search Frame to apply search filters.
        searchfrm=LabelFrame(rightframe,bd=2,borderwidth=0,relief=RIDGE,font=('Calibri',17,'bold'))
        searchfrm.place(x=0,y=0,width=640,height=40)

        srlbl=Label(searchfrm,text="Search By: ",font=('Calibri',12,'bold'),bg="brown",fg="white")
        srlbl.grid(row=0,column=0,padx=10,sticky=W)

        srcombo=ttk.Combobox(searchfrm,font=('Calibri',12),state="readonly",width=15)
        srcombo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        srcombo["values"]=("Select","Student Name","Student ID")
        srcombo.current(0)
        srcombotxt=ttk.Entry(searchfrm,width=20,font=('Calibri',12))
        srcombotxt.grid(row=0,column=2,padx=3,sticky=W)

        btnsearch=Button(searchfrm,text="Search", width=10,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnsearch.grid(row=0,column=3,padx=5)

        btnsearchall=Button(searchfrm,text="Show All", width=10,font=('Calibri',12,'bold'),bg="salmon",fg="white")
        btnsearchall.grid(row=0,column=4,padx=5)

       #Table Frame to show Data in tables.
        tblfrm=Frame(rightframe,bd=2,relief=RIDGE)
        tblfrm.place(x=0,y=70,width=640,height=400)
        
        scroll_x=ttk.Scrollbar(tblfrm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tblfrm,orient=VERTICAL)

        self.studtable = ttk.Treeview(tblfrm,column=("Name","Id","Email","Contact","Address","Gender","Course","Course_year","academic_year","semester","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studtable.xview)
        scroll_y.config(command=self.studtable.yview)

        self.studtable.heading("Name", text="Name")
        self.studtable.heading("Id", text="Id")
        self.studtable.heading("Email", text="Email")
        self.studtable.heading("Contact", text="Contact")
        self.studtable.heading("Address", text="Address")
        self.studtable.heading("Gender", text="Gender")
        self.studtable.heading("Course", text="Course")
        self.studtable.heading("Course_year", text="C_year")
        self.studtable.heading("academic_year", text="A_year")
        self.studtable.heading("semester", text="Semester")
        self.studtable.heading("photo", text="Photo")
        self.studtable["show"]="headings"
        self.studtable.pack(fill=BOTH,expand=1)
        self.studtable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #Functions to add data
    def add_data(self):
        if self.var_course.get() == "Select Course" or self.var_gender.get() == "" or self.var_address.get() == "" or self.var_ayear.get()==""or self.var_contact.get() == ""or self.var_email.get() == ""or self.var_name.get() == ""or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are reuired")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',
                                            username='root',
                                            password='Root@12345678',
                                            database='facerecognition'
                                            )
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)",(self.var_name.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_cyear.get(),
                                                                                                    self.var_ayear.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_radio1.get()
                                                                                                    
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data Added Successfully")
            except Exception as e:
                messagebox.showerror("Error",f"Error occured due to:{str(e)}",parent=self.root)  


    #Function to fetch data from database
    def fetch_data(self):  
        conn=mysql.connector.connect(host='localhost',username='root',password='Root@12345678',database='facerecognition')
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        if len(data) != 0:
            self.studtable.delete(*self.studtable.get_children())
            for i in data:
                self.studtable.insert("",END,values=i)
            conn.commit()
        conn.close()

#Get Cursor that is when you will click on the data table on the window  it will show the place that where the coloumn belongs
    def get_cursor(self,project=""):
        cursor_focus=self.studtable.focus()
        content=self.studtable.item(cursor_focus)
        datab=content["values"]
        self.var_name.set(datab[0])
        self.var_id.set(datab[1])
        self.var_email.set(datab[2])
        self.var_contact.set(datab[3])
        self.var_address.set(datab[4])
        self.var_gender.set(datab[5])
        self.var_course.set(datab[6])
        self.var_cyear.set(datab[7])
        self.var_ayear.set(datab[8])
        self.var_sem.set(datab[9])
        self.var_radio1.set(datab[10])

    #Update Function Code
    def update_data(self):
        if self.var_course.get() == "Select Course" or self.var_gender.get() == "" or self.var_address.get() == "" or self.var_ayear.get()==""or self.var_contact.get() == ""or self.var_email.get() == ""or self.var_name.get() == ""or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are reuired")
        else:
            try:
                msg_update=messagebox.askyesno("Warning","Do you want to Update the student details?",parent=self.root)
                if msg_update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Root@12345678',database='facerecognition')
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Name=%s,Email=%s,Contact=%s,Address=%s,Gender=%s,Course=%s,Cyear=%s,Ayear=%s,Semseter=%s,Photos=%s where Student_ID=%s",(self.var_name.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_contact.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_cyear.get(),
                                                                                                                                                                                                self.var_ayear.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_id.get()
                                                                                                                                                                                                ))
                else:
                    if not msg_update:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Updated student Details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Error Occured while updating: {str(e)}",parent=self.root)
    
    #Code for Delete Functions
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Please add Student_ID")
        else:
            try:
                msg_delete=messagebox.askyesno("Warning","Do you want to Delete the student details?",parent=self.root)
                if msg_delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Root@12345678',database='facerecognition')
                    mycursor=conn.cursor()
                    delt="delete from student where Student_ID = %s" 
                    val=(self.var_id.get(),)
                    mycursor.execute(delt,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully deleted student Details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Error Occured while updating: {str(e)}",parent=self.root)
            
    #Code for Reset Button
    def reset_form(self):
        self.var_name.set("")
        self.var_id.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_gender.set("")
        self.var_course.set("Select Course")
        self.var_cyear.set("F.Y")
        self.var_ayear.set("2020-21")
        self.var_sem.set("I")
        self.var_radio1.set("")

    #Function to generate dataset and photo samples
    def generate_data(self):
        if self.var_course.get() == "Select Course" or self.var_gender.get() == "" or self.var_address.get() == "" or self.var_ayear.get()==""or self.var_contact.get() == ""or self.var_email.get() == ""or self.var_name.get() == ""or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are reuired")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Root@12345678',database='facerecognition')
                mycursor=conn.cursor()
                mycursor.execute("select * from student")
                myres=mycursor.fetchall()
                id=0
                for i in myres:
                    id+=1
                mycursor.execute("update student set Name=%s,Email=%s,Contact=%s,Address=%s,Gender=%s,Course=%s,Cyear=%s,Ayear=%s,Semseter=%s,Photos=%s where Student_ID=%s",(self.var_name.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_contact.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_cyear.get(),
                                                                                                                                                                                                self.var_ayear.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_id.get()==id+1
                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_form()
                conn.close()
            # except Exception as e:
            #     messagebox.showerror("Error",f"Error Occured: {str(e)}",parent=self.root)
                # #Code to load face datasets

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def crop_face(img):
                    convgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(convgray,1.3,5)
                    # By default scaling factor is 1.3 and minimu neighbor scale is 5

                    for (x,y,w,h) in faces:
                        crop_face=img[y:y+h,x:x+w]
                        return crop_face
                
                cap=cv2.VideoCapture(0)
                idimg=0
                while True:
                    ret,photo_frame=cap.read()
                    if crop_face(photo_frame) is not None:
                        idimg+=1
                        face=cv2.resize(crop_face(photo_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="imgdata/stud."+str(id)+"."+str(idimg)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(idimg),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if int(idimg)==100 or cv2.waitKey(1)==13:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Please wait","Generating Dataset completed")
            except Exception as e:
                messagebox.showerror("Error",f"Error occured while generating data: {str(e)}",parent=self.root)


































if __name__ == "__main__":

    root =Tk()
    obj = student(root)
    root.mainloop()