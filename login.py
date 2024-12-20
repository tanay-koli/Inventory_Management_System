import email
from tkinter import*
from tkinter import messagebox
import sqlite3
import os
import pass_email
from PIL import Image, ImageTk
import smtplib #pip install smtplib
import time


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.otp=''

        #images
        self.laptop=ImageTk.PhotoImage(file="images/laptop.jpg")
        self.lbl_laptop=Label(self.root,image=self.laptop,bd=0).place(x=0,y=0)

        
        # Login_Frame
        self.emp_ID = StringVar()
        self.password = StringVar()

        login_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_Frame.place(x=950, y=110, width=350, height=460)

        title = Label(login_Frame, text="Login System",
                      font=("Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_emp_ID = Label(login_Frame, text="Employee ID", font=(
            "goudy old style", 15), bg="white", fg="#767171").place(x=25, y=110)

        txt_emp_ID = Entry(login_Frame, textvariable=self.emp_ID, font=("times new roman", 15),
                           bg="#ECECEC").place(x=50, y=140, width=250)

        lbl_pass = Label(login_Frame, text="Password", font=(
            "goudy old style", 15), bg="white", fg="#767171").place(x=25, y=210)
        txt_pass = Entry(login_Frame, textvariable=self.password, show='*', font=("times new roman", 15),
                         bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login = Button(login_Frame, command=self.login, text="Log In", font=(
            "times new roman", 17,'bold'), bg="#237cdb", activebackground="#237cdb", fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)

        hr = Label(login_Frame, bg='lightgrey').place(
            x=50, y=370, width=250, height=2)
        or_ = Label(login_Frame, text='OR', bg='white', fg="lightgrey", font=("times new roman", 15, "bold")).place(
            x=150, y=355)

        btn_forget = Button(login_Frame, text="Forgot Password?", command=self.forget_p, font=(
            "times new roman", 13), bg="white", fg="#1650d9", bd=0, activebackground="white", activeforeground="#1650d9").place(x=100, y=390)

        # Animation Images
        self.im1 = PhotoImage(file="images\login7.png")
        self.im2 = PhotoImage(file="images\image1.png")
        self.im3 = PhotoImage(file="images\login3.png")

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=250, y=150, width=520, height=380)

        self.animate()
        
# All Functions

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)

    def login(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            if self.emp_ID.get() == "" or self.password.get() == "":
                messagebox.showerror(
                    'Error', "All fields are required", parent=self.root)
            else:
                cur.execute(
                    "select UserType from employee where EmpID=? and Password=?", 
                        (self.emp_ID.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror(
                        'Error', "Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system(" dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("billing.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def forget_p(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            if self.emp_ID.get() == "":
                messagebox.showerror(
                    'Error', "Employee Id must be required", parent=self.root)
            else:
                cur.execute(
                    "select Email from employee where EmpID=?", (self.emp_ID.get()))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror(
                        'Error', "Invalid Employee ID, Try again", parent=self.root)
                else:
                    # ___Forget Window
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    # call send_email_function()
                    check=self.send_email(email[0])
                    if check=='f':
                        messagebox.showerror("Error","Connection Error, Try Again",parent=self.root)
                    else:

                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title = Label(self.forget_win, text='Reset Password', font=(
                            'goudy old style', 15, 'bold'), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                        lbl_reset = Label(self.forget_win, text="Enter OTP Sent on Regisitered Email", font=(
                            'times new roman', 15)).place(x=20, y=60)
                        txt_reset = Entry(self.forget_win, textvariable=self.var_otp, font=(
                            'times new roman', 15), bg='lightyellow').place(x=20, y=100, width=250, height=30)
                        self.btn_reset = Button(self.forget_win, text='SUBMIT',command=self.validate_otp, font=(
                            'times new roman', 15), bg='lightblue')
                        self.btn_reset.place(x=280, y=100, width=100, height=30)

                        lbl_new_pass = Label(self.forget_win, text="New Password", font=(
                            'times new roman', 15)).place(x=20, y=160)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=(
                            'times new roman', 15), bg='lightyellow').place(x=20, y=190, width=250, height=30)

                        lbl_c_pass = Label(self.forget_win, text="Confirm Password", font=(
                            'times new roman', 15)).place(x=20, y=225)
                        txt_c_pass = Entry(self.forget_win, textvariable=self.var_conf_pass, font=(
                            'times new roman', 15), bg='lightyellow').place(x=20, y=255, width=250, height=30)
                        self.btn_update = Button(self.forget_win, text='UPDATE', command=self.update_password,state=DISABLED, font=(
                            'times new roman', 15), bg='lightblue')
                        self.btn_update.place(x=150, y=300, width=100, height=30)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error, Password Is Required",parent=self.forget_win)
        elif self.var_new_pass.get()!=  self.var_conf_pass.get():
            messagebox.showerror("Error, New Password & Confirm Password Must Be Same",parent=self.forget_win)
        else:
            con = sqlite3.connect(database=r"project.db")
            cur = con.cursor()
            try:
                cur.execute("Update employee SET Password=? where EmpID=?",(self.var_new_pass.get(),self.emp_ID.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Succesfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}")


    def validate_otp(self):
        if (self.otp)==(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","INVALID OTP, Try Again",parent=self.forget_win)

    def send_email(self,to_):       
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=pass_email.email_
        password_=pass_email.password_

        s.login(email_,password_)
        self.otp=int(time.strftime("%H%M%S"))+int(time.strftime('%S'))
        
        subject="Inventory Management System Password Reset"
        message=f"Dear Sir/Ma'am, \n\n Password Reset OTP :{int(self.otp)}.\n\n "
        message="subject:{}\n\n{}".format(subject,message)
        s.sendmail(email_,to_,message)
        check=s.ehlo()
        if check[0]==250:
            return 's'
        else:
            return 'f'



root = Tk()
obj = Login_System(root)
root.mainloop()
