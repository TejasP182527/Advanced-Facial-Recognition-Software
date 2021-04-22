from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myattendencedata=[]
class student_attend:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x730+0+0")
        self.root.title("Face Recognition System")

        #Creating variables
        self.var_stud_nm=StringVar()
        self.var_stud_id=StringVar()
        self.var_stud_course=StringVar()
        self.var_stud_sem=StringVar()
        self.var_stud_time=StringVar()
        self.var_stud_date=StringVar()
        self.var_stud_status=StringVar()




        img=Image.open(r"img\h1.jpg")
        img=img.resize((1500,130))
        self.photoimg=ImageTk.PhotoImage(img)
        lblone=Label(self.root,image=self.photoimg)
        lblone.place(x=0,y=0,width=1500,height=130)


        # #Code for Background Image
        bg_img=Image.open(r"img\bg1.jpg")
        bg_img=bg_img.resize((1500,720))
        self.photobgimg=ImageTk.PhotoImage(bg_img)
        bglbl=Label(self.root,image=self.photobgimg)
        bglbl.place(x=0,y=130,width=1500,height=720)

        # #code for heading of software
        lbltitle=Label(lblone,text="STUDENT ATTENDENCE DATABASE", font=('Calibri',35,'bold'), bg='antique white',fg='black')
        lbltitle.place(x=70,y=30,width=1200,height=70)
        
        dbaseframe=Frame(bglbl,bd=2,borderwidth=0)
        dbaseframe.place(x=5,y=7,width=1345,height=580)

        leftframe=LabelFrame(bglbl,bd=2,text="Student Attendance Details:",font=('Calibri',17,'bold'),relief=RIDGE)
        leftframe.place(x=5,y=5,width=660,height=570)


        #Created frame inside left frame
        leftframe1=Frame(leftframe,bd=2,relief=RIDGE)
        leftframe1.place(x=5,y=10,width=630,height=250)

        #Add Labels and Entries
        studname=Label(leftframe1,text="Student Name: ",font=('Calibri',13))
        studname.grid(row=0,column=0,pady=8)
        studnametxt=ttk.Entry(leftframe1,textvariable=self.var_stud_nm,width=18,font=('Calibri',13))
        studnametxt.grid(row=0,column=1,padx=10,pady=8,sticky=W)

        stud_id=Label(leftframe1,text="Student ID: ",font=('Calibri',13))
        stud_id.grid(row=0,column=2,pady=8)
        stud_idtxt=ttk.Entry(leftframe1,textvariable=self.var_stud_id,width=18,font=('Calibri',13))
        stud_idtxt.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        stud_course=Label(leftframe1,text="Student Course: ",font=('Calibri',13))
        stud_course.grid(row=1,column=0,pady=8)
        stud_coursetxt=ttk.Entry(leftframe1,textvariable=self.var_stud_course,width=18,font=('Calibri',13))
        stud_coursetxt.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        stud_sem=Label(leftframe1,text="Course Sem: ",font=('Calibri',13))
        stud_sem.grid(row=1,column=2,pady=8)
        stud_semtxt=ttk.Entry(leftframe1,textvariable=self.var_stud_sem,width=18,font=('Calibri',13))
        stud_semtxt.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        att_time=Label(leftframe1,text="Attnd. Time: ",font=('Calibri',13))
        att_time.grid(row=2,column=0,pady=8)
        att_timetxt=ttk.Entry(leftframe1,textvariable=self.var_stud_time,width=18,font=('Calibri',13))
        att_timetxt.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        att_date=Label(leftframe1,text="Attnd. Date: ",font=('Calibri',13))
        att_date.grid(row=2,column=2,pady=8)
        att_datetxt=ttk.Entry(leftframe1,textvariable=self.var_stud_date,width=18,font=('Calibri',13))
        att_datetxt.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        att_status_label=Label(leftframe1,text="Attnd. Status",font=('Calibri',13))
        att_status_label.grid(row=3,column=0,padx=10,sticky=W)
        att_status=ttk.Combobox(leftframe1,textvariable=self.var_stud_status,font=('Calibri',13),state="readonly")
        att_status.grid(row=3,column=1,padx=10,pady=8,sticky=W)
        att_status["values"]=("Select","Present","Absent")
        att_status.current(0)

    #Operation Buttons
        btnframe=Frame(leftframe1,bd=2,relief=RIDGE,borderwidth=0)
        btnframe.place(x=5,y=190,width=610,height=40)

        btn_import=Button(btnframe,text="Import CSV",command=self.import_csv,width=17,font=('Calibri',12,'bold'),bg="coral",fg="white")
        btn_import.grid(row=0,column=0,padx=4)

        btn_export=Button(btnframe,text="Export CSV", command=self.export_csv,width=17,font=('Calibri',12,'bold'),bg="coral",fg="white")
        btn_export.grid(row=0,column=1,padx=4)

        btn_update=Button(btnframe,text="Update CSV",width=17,font=('Calibri',12,'bold'),bg="coral",fg="white")
        btn_update.grid(row=0,column=2,padx=4)

        btn_reset=Button(btnframe,text="Reset",command=self.reset_form,width=17,font=('Calibri',12,'bold'),bg="coral",fg="white")
        btn_reset.grid(row=0,column=3)


        #Operations on the rightframe
        right_frame=LabelFrame(bglbl,bd=2,text="Attendance Data:",font=('Calibri',17,'bold'),relief=RIDGE)
        right_frame.place(x=670,y=5,width=660,height=570)

        rightframe1=Frame(right_frame,bd=2,relief=RIDGE)
        rightframe1.place(x=5,y=10,width=630,height=500)

        #Adding scroll bar for attendence_report
        scroll_x=ttk.Scrollbar(rightframe1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(rightframe1,orient=VERTICAL)

        self.attendence_report=ttk.Treeview(rightframe1,column=("Name","Student_Id","Course","Semester","Attend Time","Attend Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendence_report.xview)
        scroll_y.config(command=self.attendence_report.yview)

        self.attendence_report.heading("Name", text="Name")
        self.attendence_report.heading("Student_Id", text="Student Id")
        self.attendence_report.heading("Course", text="Course")
        self.attendence_report.heading("Semester", text="Semester")
        self.attendence_report.heading("Attend Time", text="Attend Time")
        self.attendence_report.heading("Attend Date", text="Attend Date")
        self.attendence_report.heading("Status", text="Status")

        self.attendence_report["show"]="headings"
        self.attendence_report.column("Name",width=80)
        self.attendence_report.column("Student_Id",width=80)
        self.attendence_report.column("Course",width=80)
        self.attendence_report.column("Semester",width=80)
        self.attendence_report.column("Attend Time",width=80)
        self.attendence_report.column("Attend Date",width=80)
        self.attendence_report.column("Status",width=80)
    
        self.attendence_report.pack(fill=BOTH,expand=1)
        self.attendence_report.bind("<ButtonRelease>",self.get_cursor_position)

    #Fetching Attendance Database
    def data_fetch(self,rows):
        self.attendence_report.delete(*self.attendence_report.get_children())
        for i in rows:
            self.attendence_report.insert("",END,values=i)

    #To import data from created csv file
    def import_csv(self):
        global myattendencedata
        myattendencedata.clear()
        filenm=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(filenm) as myfile:
            read_csv=csv.reader(myfile,delimiter=",")
            for i in read_csv:
                myattendencedata.append(i)
            self.data_fetch(myattendencedata)

    def export_csv(self):
        try:
            if len(myattendencedata)<1:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            filenm=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(filenm,mode="w",newline="") as myfile:
                writeto_csv=csv.writer(myfile,delimiter=",")
                for i in myattendencedata:
                    writeto_csv.writerow(i)
                messagebox.showinfo("Done","Data Exported successfully to"+os.path.basename(filenm))
        except Exception as e:
            messagebox.showerror("Error",f"Error occured due to:{str(e)}",parent=self.root)

    #function to get cursor position
    def get_cursor_position(self,project=""):
        cursor_row=self.attendence_report.focus()
        content_row=self.attendence_report.item(cursor_row)
        rows=content_row['values']
        self.var_stud_nm.set(rows[0])
        self.var_stud_id.set(rows[1])
        self.var_stud_course.set(rows[2])
        self.var_stud_sem.set(rows[3])
        self.var_stud_time.set(rows[4])
        self.var_stud_date.set(rows[5])
        self.var_stud_status.set(rows[6])

    #Function to clear form
    def reset_form(self,project=""):
        self.var_stud_nm.set("")
        self.var_stud_id.set("")
        self.var_stud_course.set("")
        self.var_stud_sem.set("")
        self.var_stud_time.set("")
        self.var_stud_date.set("")
        self.var_stud_status.set("Select")





        
























































if __name__ == "__main__":
    root =Tk()
    obj = student_attend(root)
    root.mainloop()
