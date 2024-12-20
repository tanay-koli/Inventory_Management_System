from ast import Delete
import sqlite3
from tkinter import *
from tkinter import font
from turtle import width
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CategoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(width=FALSE,height=FALSE)
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()
#Variable
        self.var_CategoryID=StringVar()
        self.var_Name=StringVar()

#title
        lbl_title=Label(self.root,text="Manage Product Categories",font=("goudy old style",35,"bold"),bg="Dark Green",fg="White",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=5)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",25,"bold"),bg="white").place(x=50,y=110)
        txt_name=Entry(self.root,textvariable=self.var_Name,font=("goudy old style",20,"bold"),bg="light yellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15,'bold'),bg="blue",fg="black",cursor="hand2").place(x=360,y=169,width=150,height=30)
        btn_update=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,'bold'),bg="red",fg="black",cursor="hand2").place(x=520,y=169,width=150,height=30)


#CategoryDetails
        cat_frame=Frame(self.root,bd=4,relief=RIDGE)
        cat_frame.place(x=700,y=90,width=380,height=110)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CatTable=ttk.Treeview(cat_frame,columns=("Category ID","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CatTable.xview)
        scrolly.config(command=self.CatTable.yview)
        self.CatTable.heading("Category ID",text="Category ID")
        self.CatTable.heading("Name",text="Name")
        
       
        self.CatTable["show"]="headings"

        self.CatTable.column("Category ID",width=100)
        self.CatTable.column("Name",width=100)
        

        self.CatTable.pack(fill=BOTH,expand=1)
        self.CatTable.bind('<ButtonRelease-1>',self.get_data)

#image
        self.Image=Image.open("images/image1.png")
        self.Image=self.Image.resize((500,250),Image.ANTIALIAS)
        self.Image=ImageTk.PhotoImage(self.Image)

        self.lbl_Image=Label(self.root,image=self.Image,bd=2,relief=RAISED)
        self.lbl_Image.place(x=50,y=220)

        self.Image2=Image.open("images/image1.jpg")
        self.Image2=self.Image2.resize((500,250),Image.ANTIALIAS)
        self.Image2=ImageTk.PhotoImage(self.Image2)

        self.lbl_Image2=Label(self.root,image=self.Image2,bd=2,relief=RAISED)
        self.lbl_Image2.place(x=580,y=220)

        self.show()


#functions
    def add(self):
            con=sqlite3.connect(database=r"project.db")
            cur=con.cursor()
            try:
                if self.var_Name.get()=="":
                    messagebox.showerror("Error","Category Name Must Be Required",parent=self.root)
                else:
                    cur.execute("Select * from Category where Name=?",(self.var_Name.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","This Category is Already Present, Try A Different One",parent=self.root)
                    else:
                        cur.execute("Insert into Category(Name) values(?)",(self.var_Name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category Added Sucessfully",parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}")





    def show(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from Category")
            rows=cur.fetchall()
            self.CatTable.delete(*self.CatTable.get_children())
            for row in rows:
                self.CatTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def get_data(self,ev):
        f=self.CatTable.focus()
        content=(self.CatTable.item(f))
        row=content['values']
        #print(row)
        self.var_CategoryID.set(row[0])
        self.var_Name.set(row[1]),

    def delete(self):
            con=sqlite3.connect(database=r"project.db")
            cur=con.cursor()
            try:
                if self.var_CategoryID.get()=="":
                    messagebox.showerror("Error","Category Name Must Be Required",parent=self.root)
                else:
                    cur.execute("Select * from Category where CatID=?",(self.var_CategoryID.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Category , Try A Different One",parent=self.root)
                    
                    else:
                        op=messagebox.askyesno("Confirm","Do You Really Want To Delete?",parent=self.root)    
                        if op==True:
                            cur.execute("delete from category where CatID=?",(self.var_CategoryID.get(),))
                            con.commit()
                            messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                            self.clear()
                            self.var_CategoryID.set("")
                            self.var_Name.set("")
                            
    
    
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}")        
        
    def clear(self):
        self.var_Name.set("")
        self.var_CategoryID.set("")
        self.show()        

    
if __name__=="__main__":       
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()