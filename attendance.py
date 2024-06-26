from tkinter import*
from tkinter import ttk

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
#first image
        img = Image.open("images/img_12.png")
        img = img.resize((800, 200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=0, y=0, width=800, height=200)

        # image 2
        img1 = Image.open("images/img_13.png")
        img1 = img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=800, y=0, width=800, height=200)
        # background
        img3 = Image.open("images/img_4.png")
        img3 = img3.resize((1450, 650))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        # f_lbl= Label(self.root, text = "First name")
        bg_img.place(x=0, y=120, width=1400, height=650)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1450, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=650)

#LEFT FRAME
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student_Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open("images/img_14.png")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=700, height=115)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=710, height=300)

        #LEFTLABEL ENTRY
        #attendence id
        attendenceId_label = Label(left_inside_frame, text="AttendanceID", font=("times new roman", 12, "bold"), bg='white')
        attendenceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendenceId_entry = ttk.Entry(left_inside_frame,  width=20,
                                    font=("times new roman", 12, "bold"))
        attendenceId_entry.grid(row=0, column=1, padx=10, sticky=W)
        #NAME
        name_label = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"),
                                   bg='white')
        name_label.grid(row=0, column=2, padx=10, sticky=W)

        nameentry = ttk.Entry(left_inside_frame, width=20,
                                       font=("times new roman", 12, "bold"))
        nameentry.grid(row=0, column=3, padx=10, sticky=W)
        #DATE
        date_label = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"),
                                   bg='white')
        date_label.grid(row=1, column=0, padx=10, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20,
                                       font=("times new roman", 12, "bold"))
        date_entry.grid(row=1, column=1, padx=10, sticky=W)
       #Department
        department_label = Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"),
                                   bg='white')
        department_label.grid(row=1, column=2, padx=10, sticky=W)

        department_entry = ttk.Entry(left_inside_frame, width=20,
                                       font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, sticky=W)
        #time
        time_label = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"),
                                   bg='white')
        time_label.grid(row=2, column=0, padx=10, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20,
                                       font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, sticky=W)
        #date
        roll_label = Label(left_inside_frame, text="Rollno", font=("times new roman", 12, "bold"),
                           bg='white')
        roll_label.grid(row=2, column=2, padx=10, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 12, "bold"))
        roll_entry.grid(row=2, column=3, padx=10, sticky=W)

        #attendance
        attendenceId_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"),
                                   bg='white')
        attendenceId_label.grid(row=3, column=0, padx=10, sticky=W)
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=720, height=45)  # CODE CHANGE HERE
        # BOTTOM BUTTON CREATE
        save_btn = Button(btn_frame, text="Import csv",  width=10, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # update
        update_btn = Button(btn_frame, text="Export csv", width=10,
                            font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        # delete
        delete_btn = Button(btn_frame, text="Update",  width=10,
                            font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        # reset
        reset_btn = Button(btn_frame, text="Reset",  width=10,
                           font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)  #


if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
