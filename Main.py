from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

class FaceRecognitionSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
        
        img=Image.open("images/img.png")
        img = img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        #f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=0,y=0,width=500,height=130)    

#image 2
        img1 = Image.open("images/img_1.png")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=500, y=0, width=500, height=130)
#image 3
        img2 = Image.open("images/img_3.png")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl= Label(self.root, text = "First name")
        f_lbl.place(x=1000, y=0, width=400, height=130)
#background image
        img3 = Image.open("images/img_4.png")
        img3 = img3.resize((1450, 650))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        # f_lbl= Label(self.root, text = "First name")
        bg_img.place(x=0, y=120, width=1400, height=650)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1450,height=45)
#student button
        img4 = Image.open("images/img_5.png")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,cursor="hand2", command = self.std_button)
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img,text="Student Data", cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)
    #Detection Button
        img5 = Image.open("images/img_6.png")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face detection", cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=300, width=220, height=40)

        #Attendence button
        img6 = Image.open("images/img_7.png")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendence", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)

        #Help Desk
        img7 = Image.open("images/img_8.png")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=1100, y=300, width=220, height=40)
        #Train Data
        img8 = Image.open("images/img_9.png")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=350, width=220, height=160)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=200, y=500, width=220, height=45)
        #PHOTOS Button
        img9 = Image.open("images/img_10.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=350, width=220, height=160)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=500, width=220, height=45)

        #EXIT button
        img10 = Image.open("images/img_11.png")
        img10= img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=350, width=220, height=160)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=800, y=500, width=220, height=45)
    def open_img(self):
        os.startfile("data")

        #========================function button=================
    def std_button(self):
        print ("Printing student data:")
        std = Student(root)
        std.root.mainloop()

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)





if __name__== "__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()