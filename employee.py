from ast import Delete
import sqlite3
from tkinter import *
from tkinter import font
from turtle import width
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class EmpClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(width=FALSE,height=FALSE)
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()
        #AllVariables
        self.var_SearchBy=StringVar()
        self.var_SearchTxt=StringVar()
        self.var_EmpID=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact=StringVar()
        self.var_Name=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Email=StringVar()
        self.var_Password=StringVar()
        self.var_UserType=StringVar()
        self.var_Address=StringVar()
        self.var_Salary=StringVar()
    

        #searchframe
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,'bold'),bd=3,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #options
        cmb_searchbox=ttk.Combobox(SearchFrame,textvariable=self.var_SearchBy,values=("Select","Name",'Email',"Contact"),state="readonly",justify=CENTER,font=("goudy old style",15,'bold'))
        cmb_searchbox.place(x=10,y=10,width=180)
        cmb_searchbox.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_SearchTxt,font=("goudy old style",15,'bold'),bg="silver").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15,'bold'),bg="yellow green",fg="black",cursor="hand2").place(x=430,y=7,width=130,height=30)

        #title
        title=Label(self.root,text="Employee Details",font=("goudy old style",15,"bold"),bg="Dark Blue",fg="White").place(x=50,y=100,width=1000)

        #content
        #row1
        lbl_EmpID=Label(self.root,text="Employee ID",font=("goudy old style",15,"bold"),bg="White")
        lbl_EmpID.place(x=50,y=150)
        lbl_Gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="White").place(x=410,y=150)
        lbl_Contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="White").place(x=750,y=150)

        txt_EmpID=Entry(self.root,textvariable=self.var_EmpID,font=("goudy old style",15,'bold'),bg="silver")
        txt_EmpID.place(x=180,y=150,width=180)
        #txt_Gender=Entry(self.root,textvariable=self.var_Gender,font=("goudy old style",15,'bold'),bg="silver").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_Gender,values=("Select","Male",'Female',"Other"),state="readonly",justify=CENTER,font=("goudy old style",15,'bold'))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_Contact=Entry(self.root,textvariable=self.var_Contact,font=("goudy old style",15,'bold'),bg="silver").place(x=830,y=150,width=180)

        #row2
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=190)
        lbl_DateOfBirth=Label(self.root,text="D.O.B.",font=("goudy old style",15,"bold"),bg="White").place(x=410,y=190)
        lbl_DateOfJoining=Label(self.root,text="D.O.J.",font=("goudy old style",15,"bold"),bg="White").place(x=750,y=190)

        txt_Name=Entry(self.root,textvariable=self.var_Name,font=("goudy old style",15,'bold'),bg="silver").place(x=180,y=190,width=180)
        txt_DateOfBirth=Entry(self.root,textvariable=self.var_DOB,font=("goudy old style",15,'bold'),bg="silver").place(x=500,y=190,width=180)
        txt_DateOfJoining=Entry(self.root,textvariable=self.var_DOJ,font=("goudy old style",15,'bold'),bg="silver").place(x=830,y=190,width=180)

        #row3
        lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=230)
        lbl_Password=Label(self.root,text="Password",font=("goudy old style",15,"bold"),bg="White")
        lbl_Password.place(x=410,y=230)
        lbl_Usertype=Label(self.root,text="Usertype",font=("goudy old style",15,"bold"),bg="White").place(x=750,y=230)

        txt_Email=Entry(self.root,textvariable=self.var_Email,font=("goudy old style",15,'bold'),bg="silver").place(x=180,y=230,width=180)
        txt_Password=Entry(self.root,textvariable=self.var_Password,font=("goudy old style",15,'bold'),bg="silver")
        txt_Password.place(x=500,y=230,width=180)
        cmb_UserType=ttk.Combobox(self.root,textvariable=self.var_UserType,values=("Select","Admin",'Employee'),state="readonly",justify=CENTER,font=("goudy old style",15,'bold'))
        cmb_UserType.place(x=830,y=230,width=180)
        cmb_UserType.current(0)

        #row4
        lbl_Address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=270)
        lbl_Salary=Label(self.root,text="Salary",font=("goudy old style",15,"bold"),bg="White").place(x=650,y=270)
        
        self.txt_Address=Text(self.root,font=("goudy old style",15,'bold'),bg="silver")
        self.txt_Address.place(x=180,y=270,width=400,height=70)
        txt_Salary=Entry(self.root,textvariable=self.var_Salary,font=("goudy old style",15,'bold'),bg="silver").place(x=720,y=270,width=180)
        
        #button
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,'bold'),bg="blue",fg="black",cursor="hand2").place(x=600,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,'bold'),bg="red",fg="black",cursor="hand2").place(x=720,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,'bold'),bg="green",fg="black",cursor="hand2").place(x=840,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,'bold'),bg= "brown",fg="black",cursor="hand2").place(x=960,y=305,width=110,height=28)
        
        #EmployeeDetails
        emp_frame=Frame(self.root,bd=4,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmpTable=ttk.Treeview(emp_frame,columns=("Employee ID","Name","Email","Gender","Contact","DOB","DOJ","Password","UserType","Address","Salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmpTable.xview)
        scrolly.config(command=self.EmpTable.yview)
        self.EmpTable.heading("Employee ID",text="Employee ID")
        self.EmpTable.heading("Name",text="Name")
        self.EmpTable.heading("Email",text="Email")
        self.EmpTable.heading("Gender",text="Gender")
        self.EmpTable.heading("Contact",text="Contact")
        self.EmpTable.heading("DOB",text="Date Of Birth")
        self.EmpTable.heading("DOJ",text="Date Of Joining")
        self.EmpTable.heading("Password",text="Password")
        self.EmpTable.heading("UserType",text="UserType")
        self.EmpTable.heading("Address",text="Address")
        self.EmpTable.heading("Salary",text="Salary")
       
        self.EmpTable["show"]="headings"

        self.EmpTable.column("Employee ID",width=90)
        self.EmpTable.column("Name",width=100)
        self.EmpTable.column("Email",width=100)
        self.EmpTable.column("Gender",width=100)
        self.EmpTable.column("Contact",width=100)
        self.EmpTable.column("DOB",width=100)
        self.EmpTable.column("DOJ",width=100)
        self.EmpTable.column("Password",width=100)
        self.EmpTable.column("UserType",width=100)
        self.EmpTable.column("Address",width=100)
        self.EmpTable.column("Salary",width=100)

        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()

#____
    def add(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_EmpID.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where EmpID=?",(self.var_EmpID.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is Already Assigned, Try A Different One",parent=self.root)
                else:
                    cur.execute("Insert into employee (EmpID,Name,Email,Gender,Contact,DOB,DOJ,Password,UserType,Address,Salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                self.var_EmpID.get(),
                                self.var_Name.get(),
                                self.var_Email.get(),
                                self.var_Gender.get(),
                                self.var_Contact.get(),
                                self.var_DOB.get(),
                                self.var_DOJ.get(),
                                self.var_Password.get(),
                                self.var_UserType.get(),
                                self.txt_Address.get("1.0",END),
                                self.var_Salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmpTable.delete(*self.EmpTable.get_children())
            for row in rows:
                self.EmpTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def get_data(self,ev):
        f=self.EmpTable.focus()
        content=(self.EmpTable.item(f))
        row=content['values']
        #print(row)
        self.var_EmpID.set(row[0])
        self.var_Name.set(row[1])
        self.var_Email.set(row[2])
        self.var_Gender.set(row[3])
        self.var_Contact.set(row[4])
        self.var_DOB.set(row[5])
        self.var_DOJ.set(row[6])
        self.var_Password.set(row[7])
        self.var_UserType.set(row[8])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[9])
        self.var_Salary.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_EmpID.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where EmpID=?",(self.var_EmpID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, Try A Different One",parent=self.root)
                else:
                    cur.execute("Update employee set Name=?,Email=?,Gender=?,Contact=?,DOB=?,DOJ=?,Password=?,UserType=?,Address=?,Salary=? where EmpID=?",(            
                                    self.var_Name.get(),
                                    self.var_Email.get(),
                                    self.var_Gender.get(),
                                    self.var_Contact.get(),
                                    self.var_DOB.get(),
                                    self.var_DOJ.get(),
                                    self.var_Password.get(),
                                    self.var_UserType.get(),
                                    self.txt_Address.get("1.0",END),
                                    self.var_Salary.get(),
                                    self.var_EmpID.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")        
    
    def delete(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_EmpID.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where EmpID=?",(self.var_EmpID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, Try A Different One",parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where EmpID=?",(self.var_EmpID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Delted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")        
    
    def clear(self):
        self.var_Name.set("")
        self.var_Email.set("")
        self.var_Gender.set("Select")
        self.var_Contact.set("")
        self.var_DOB.set("")
        self.var_DOJ.set("")
        self.var_Password.set("")
        self.var_UserType.set("Admin")
        self.txt_Address.delete("1.0",END)
        self.var_Salary.set("")
        self.var_EmpID.set("")  
        self.var_SearchTxt.set("")  
        self.var_SearchBy.set("Select")
        self.show()                                                                                                             
                        

    def search(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_SearchBy.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_SearchTxt.get()=="":
                messagebox.showerror("Error","Search Input Should Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where "+self.var_SearchBy.get()+" LIKE '%"+self.var_SearchTxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmpTable.delete(*self.EmpTable.get_children())
                    for row in rows:
                        self.EmpTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

        
        



if __name__=="__main__":       
    root=Tk()
    obj=EmpClass(root)
    root.mainloop()