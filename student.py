'''from tkinter import*
from tkinter import ttk

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        #========================variable=====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img = Image.open("images/img_12.png")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=0, y=0, width=500, height=130)

        # image 2
        img1 = Image.open("images/img_13.png")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=500, y=0, width=500, height=130)
        # image 3
        img2 = Image.open("images/img_14.png")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=1000, y=0, width=400, height=130)

        #background
        img3 = Image.open("images/img_4.png")
        img3 = img3.resize((1450, 650))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        # f_lbl= Label(self.root, text = "First name")
        bg_img.place(x=0, y=120, width=1400, height=650)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1450, height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1500,height=650)
        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open("images/img_14.png")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=700, height=115)

        #Current Course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course Info",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)
        #DEPARTMENT
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","MCA","Btech-ECE","IT","CSE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)
        #COURSE#changement done======
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,text="Course", font=("times new roman", 12, "bold"), width=17,
                                 state="read only")
        course_combo["values"] = ("Select Course", "MCA-IA","MCA-2A","Btech-ECE", "AI", "ML","DS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3)

        #Year
        year_label=Label(current_course_frame,text="Year", font=("times new roman", 12, "bold"),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("select year","2019-2020","2020-2021","2021-2022","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,sticky=W)

        #semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17,
                                  state="read only")
        semester_combo["values"] = ("select semester", "semester-1", "semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, sticky=W)
        #Studen Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class StuInfo",
                                          font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=230, width=720, height=300)
         #Student ID
        studentId_label = Label(class_student_frame, text="StudentID", font=("times new roman", 12, "bold"), bg='white')
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10, sticky=W)

        #Student Name

        studentName_label = Label(class_student_frame, text="StudentName", font=("times new roman", 12, "bold"), bg='white')
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
        #class division

        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"),
                                  bg='white')
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

       # class_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        #class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"), width=17, state="read only")
        div_combo["values"] = ("A", "B","C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, sticky=W)
        #Roll no
        roll_no_label = Label(class_student_frame, text="Roll NO", font=("times new roman", 12, "bold"),
                                  bg='white')
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        #Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"),
                                  bg='white')
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        #gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        #gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), width=17, state="read only")
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W)

        #dob
        dob_label = Label(class_student_frame, text="D.O.B", font=("times new roman", 12, "bold"),
                                  bg='white')
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        #EMAIL
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"),
                                  bg='white')
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        #Phone NUMBER
        phone_label = Label(class_student_frame, text="Mob NO", font=("times new roman", 12, "bold"),
                                  bg='white')
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        #Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"),
                                  bg='white')
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        #Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"),
                                  bg='white')
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        #Radio BUtton
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)
        #change done in previous code

        #review text variable nhi liya radio2 me
        radionbtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radionbtn2.grid(row=5, column=1)
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=720,height=45)#CODE CHANGE HERE
         # BOTTOM BUTTON CREATE
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #update
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        #delete
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        #reset
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        #take photo
        take_btn = Button(btn_frame,command=self.generate_dataset,text="TakePhoto Sample", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_btn.grid(row=0, column=4)
        #Update Photo
        update_btn = Button(btn_frame, text="UpdatePhoto Sample", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=5)

        #Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)#

        img_right = Image.open("images/img_14.png")
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=700, height=115)
        #==============SEARCH SYSTEM=============================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                            bg='red',fg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17,
                                      state="read only")
        search_combo["values"] = ("select", "Roll no", "Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame, width=13, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)





        search_btn = Button(search_frame, text="Search", width=10, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3)

        showall_btn = Button(search_frame, text="Show All", width=10, font=("times new roman", 10, "bold"), bg="blue",
                           fg="white")
        showall_btn.grid(row=0, column=4)
        #=============================TABLE FRAME ======================================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=200, width=650, height=260)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Courses")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()###
        #for data fetch additional
    #=================FUNCTION DECLERATION===========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        else:
            try:
              conn=mysql.connector.connect(host="localhost",user="root",password="Dixit@123",database="face_recogniser")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                     self.var_dep.get(),
                     self.var_course.get(),
                     self.var_year.get(),
                     self.var_semester.get(),
                     self.var_std_id.get(),
                     self.var_std_name.get(),
                     self.var_div.get(),
                     self.var_roll.get(),
                     self.var_gender.get(),
                     datetime.strptime(self.var_dob.get(), "%Y-%m-%d"),
                     self.var_email.get(),
                     self.var_phone.get(),
                     self.var_address.get(),
                     self.var_teacher.get(),
                     self.var_radio1.get()#REVIEW


                        ))
              conn.commit()
              self.fetch_data()##
              conn.close()
              messagebox.showinfo("sucess","student details added successfully",parent=self.root)
            except Exception as es:
              messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

#==================FETCH FROM DATABASE==========================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Dixit@123", database="face_recogniser")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

     #===================get cursor======for update=======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    #update function +++++++
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update>0:
                   conn = mysql.connector.connect(host="localhost", user="root", password="Dixit@123",
                                           database="face_recogniser")
                   my_cursor = conn.cursor()
                   my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,division=%s,rollno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                       self.var_dep.get(),
                       self.var_course.get(),
                       self.var_year.get(),
                       self.var_semester.get(),
                       self.var_div.get(),
                       self.var_roll.get(),
                       self.var_gender.get(),
                       datetime.strptime(self.var_dob.get(), "%Y-%m-%d %H:%M:%S"),
                       self.var_email.get(),
                       self.var_phone.get(),
                       self.var_address.get(),
                       self.var_teacher.get(),
                       self.var_radio1.get(),
                       self.var_std_id.get(),
                       # REVIEW

                       # update function +++++++
                   ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","student detais succesfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

#===============delete function================================
    def delete_data(self):
        if self.var_std_id.get()=="":##========
            messagebox.showerror("Error","Student id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","do you wnt to delete",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Dixit@123",
                                           database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id =%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
#===========reset data====================
    def reset_data(self):
        self.var_dep.set("select Department"),
        self.var_course.set("select course"),
        self.var_year.set("select year"),
        self.var_semester.set("select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("select division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


#==========================Generate  data set or take photo sample================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All field required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Dixit@123",
                                                   database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute(
                     "update student set Dep=%s,course=%s,year=%s,semester=%s,division=%s,rollno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                   # self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    datetime.strptime(self.var_dob.get(), "%Y-%m-%d %H:%M:%S"),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                    # REVIEW

                    # update function +++++++
                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            #============load predefined data on face frontals ======from opencv========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scale factor=1.3
                    #min neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
               # cv2.face.LBPHFaceRecognizer_create()
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)












if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()'''

from tkinter import*
from tkinter import ttk
from modules.dbconnect import *
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        #========================variable=====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img = Image.open("images/img_12.png")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=0, y=0, width=500, height=130)

        # image 2
        img1 = Image.open("images/img_13.png")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=500, y=0, width=500, height=130)
        # image 3
        img2 = Image.open("images/img_14.png")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=1000, y=0, width=400, height=130)

        #background
        img3 = Image.open("images/img_4.png")
        img3 = img3.resize((1450, 650))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        # f_lbl= Label(self.root, text = "First name")
        bg_img.place(x=0, y=120, width=1400, height=650)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1450, height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1500,height=650)
        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open("images/img_14.png")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=700, height=115)

        #Current Course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course Info",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)
        #DEPARTMENT
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","MCA","Btech-ECE","IT","CSE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)
        #COURSE#changement done======
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,text="Course", font=("times new roman", 12, "bold"), width=17,
                                 state="read only")
        course_combo["values"] = ("Select Course", "MCA-IA","MCA-2A","Btech-ECE", "AI", "ML","DS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3)

        #Year
        year_label=Label(current_course_frame,text="Year", font=("times new roman", 12, "bold"),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("select year","2019-2020","2020-2021","2021-2022","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,sticky=W)

        #semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17,
                                  state="read only")
        semester_combo["values"] = ("select semester", "semester-1", "semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, sticky=W)
        #Studen Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class StuInfo",
                                          font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=230, width=720, height=300)
         #Student ID
        studentId_label = Label(class_student_frame, text="StudentID", font=("times new roman", 12, "bold"), bg='white')
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"),state="readonly")
        studentID_entry.grid(row=0,column=1,padx=10, sticky=W)
        #=================
        my_cursor.execute("select max(student_id) from student;")
        print ()
        my_tuple = my_cursor.fetchone()
        print("fetchone: ", my_tuple)
        if my_tuple[0] > 0:
            std_id = my_tuple[0] + 1

        else:
            std_id = 1

        self.var_std_id.set(std_id)

        #Student Name

        studentName_label = Label(class_student_frame, text="StudentName", font=("times new roman", 12, "bold"), bg='white')
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
        #class division

        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"),
                                  bg='white')
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

       # class_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        #class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"), width=17, state="read only")
        div_combo["values"] = ("A", "B","C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, sticky=W)
        #Roll no
        roll_no_label = Label(class_student_frame, text="Roll NO", font=("times new roman", 12, "bold"),
                                  bg='white')
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        #Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"),
                                  bg='white')
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        #gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        #gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), width=17, state="read only")
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W)

        #dob
        dob_label = Label(class_student_frame, text="D.O.B", font=("times new roman", 12, "bold"),
                                  bg='white')
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        #EMAIL
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"),
                                  bg='white')
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        #Phone NUMBER
        phone_label = Label(class_student_frame, text="Mob NO", font=("times new roman", 12, "bold"),
                                  bg='white')
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        #Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"),
                                  bg='white')
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        #Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"),
                                  bg='white')
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        #Radio BUtton
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)
        #change done in previous code

        #review text variable nhi liya radio2 me
        radionbtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radionbtn2.grid(row=5, column=1)
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=720,height=45)#CODE CHANGE HERE
         # BOTTOM BUTTON CREATE
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #update
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        #delete
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        #reset
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        #take photo
        take_btn = Button(btn_frame,command=self.generate_dataset,text="TakePhoto Sample", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_btn.grid(row=0, column=4)
        #Update Photo
        update_btn = Button(btn_frame, text="UpdatePhoto Sample", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=5)

        #Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)#

        img_right = Image.open("images/img_14.png")
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=700, height=115)
        #==============SEARCH SYSTEM=============================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                            bg='red',fg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17,
                                      state="read only")
        search_combo["values"] = ("select", "Roll no", "Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame, width=13, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)





        search_btn = Button(search_frame, text="Search", width=10, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3)

        showall_btn = Button(search_frame, text="Show All", width=10, font=("times new roman", 10, "bold"), bg="blue",
                           fg="white")
        showall_btn.grid(row=0, column=4)
        #=============================TABLE FRAME ======================================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=200, width=650, height=260)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Courses")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()###
        #for data fetch additional
    #=================FUNCTION DECLERATION===========

    def add_data(self):
        from modules import dbconnect
        print ("cursor: ", dbconnect.my_cursor)
        # if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "":
            messagebox.showerror("Error","All field required",parent=self.root)
        else:
            try:
              my_cursor.execute("insert into student (Dep, course, year, semester, name, division, rollno, gender, dob, email, phone, address, teacher, photosample)"
                                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                     self.var_dep.get(),
                     self.var_course.get(),
                     self.var_year.get(),
                     self.var_semester.get(),
                     self.var_std_name.get(),
                     self.var_div.get(),
                     self.var_roll.get(),
                     self.var_gender.get(),
                     datetime.strptime(self.var_dob.get(), "%Y-%m-%d"),
                     self.var_email.get(),
                     self.var_phone.get(),
                     self.var_address.get(),
                     self.var_teacher.get(),
                     self.var_radio1.get()#REVIEW


                        ))
              conn.commit()
              self.fetch_data()##
              #my_cursor.close()
              #conn.close()
              messagebox.showinfo("sucess","student details added successfully",parent=self.root)
            except Exception as es:
              messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

#==================FETCH FROM DATABASE==========================================
    def fetch_data(self):
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        #my_cursor.close()
        #conn.close()

     #===================get cursor======for update=======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    #update function +++++++
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update>0:
                   my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,rollno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                       self.var_dep.get(),                                                    ##name is added in previous code##
                       self.var_course.get(),
                       self.var_year.get(),
                       self.var_semester.get(),
                       self.var_std_name.get(),######
                       self.var_div.get(),
                       self.var_roll.get(),
                       self.var_gender.get(),
                       datetime.strptime(self.var_dob.get(), "%Y-%m-%d %H:%M:%S"),
                       self.var_email.get(),
                       self.var_phone.get(),
                       self.var_address.get(),
                       self.var_teacher.get(),
                       self.var_radio1.get(),
                       self.var_std_id.get(),
                       # REVIEW

                       # update function +++++++
                   ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","student detais succesfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                my_cursor.close()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

#===============delete function================================
    def delete_data(self):
        if self.var_std_id.get()=="":##========
            messagebox.showerror("Error","Student id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","do you wnt to delete",parent=self.root)
                if delete>0:
                    sql="delete from student where student_id =%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                my_cursor.close()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
#===========reset data====================
    def reset_data(self):
        self.var_dep.set("select Department"),
        self.var_course.set("select course"),
        self.var_year.set("select year"),
        self.var_semester.set("select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("select division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


#==========================Generate  data set or take photo sample================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All field required", parent=self.root)
        else:
            try:
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute(
                     "update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,rollno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",
                (                                                             #=====name===
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),#=========name=====
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    datetime.strptime(self.var_dob.get(), "%Y-%m-%d %H:%M:%S"),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                    # REVIEW

                    # update function +++++++
                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                my_cursor.close()
                conn.close()
            #============load predefined data on face frontals ======from opencv========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scale factor=1.3
                    #min neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
               # cv2.face.LBPHFaceRecognizer_create()
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)












if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()