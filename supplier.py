from ast import Delete
import sqlite3
from tkinter import *
from tkinter import font
from turtle import width
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
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
        self.var_SupInvoice=StringVar()
        self.var_SuppName=StringVar()
        self.var_Contact=StringVar()
        
    


        #options
        lbl_searchbox=Label(self.root,text="Invoice Number",font=("goudy old style",15,'bold'))
        lbl_searchbox.place(x=670,y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_SearchTxt,font=("goudy old style",15,'bold'),bg="light yellow").place(x=820,y=80,width=150)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="gold",fg="black",cursor="hand2").place(x=990,y=79,width=100,height=27)

        #title
        title=Label(self.root,text="Supplier Details",font=("goudy old style",25,"bold"),bg="Dark Blue",fg="White").place(x=50,y=10,width=1000,height=40)

        #content
        #row1
        lbl_SuppInvoice=Label(self.root,text="Invoice Number",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=70)
        txt_SuppInvoice=Entry(self.root,textvariable=self.var_SupInvoice,font=("goudy old style",15,'bold'),bg="light yellow").place(x=200,y=70,width=220)
        

        #row2
        lbl_SuppName=Label(self.root,text="Supplier Name",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=110)
        txt_SuppName=Entry(self.root,textvariable=self.var_SuppName,font=("goudy old style",15,'bold'),bg="light yellow").place(x=200,y=110,width=220)
        

        #row3
        lbl_Contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=150)
        txt_Contact=Entry(self.root,textvariable=self.var_Contact,font=("goudy old style",15,'bold'),bg="light yellow").place(x=200,y=150,width=220)
        

        #row4
        lbl_Address=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="White").place(x=50,y=190)
        self.txt_Address=Text(self.root,font=("goudy old style",15,'bold'),bg="light yellow")
        self.txt_Address.place(x=200,y=190,width=430,height=100)
                
        #button
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,'bold'),bg="blue",fg="black",cursor="hand2").place(x=200,y=345,width=100,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,'bold'),bg="red",fg="black",cursor="hand2").place(x=310,y=345,width=100,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,'bold'),bg="green",fg="black",cursor="hand2").place(x=420,y=345,width=100,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,'bold'),bg= "brown",fg="black",cursor="hand2").place(x=530,y=345,width=100,height=40)
        
        #EmployeeDetails
        emp_frame=Frame(self.root,bd=4,relief=RIDGE)
        emp_frame.place(x=670,y=120,width=420,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SuppTable=ttk.Treeview(emp_frame,columns=("Supplier Invoice","Supplier Name","Contact","Description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SuppTable.xview)
        scrolly.config(command=self.SuppTable.yview)
        self.SuppTable.heading("Supplier Invoice",text="Supplier Invoice")
        self.SuppTable.heading("Supplier Name",text="Supplier Name")
        self.SuppTable.heading("Contact",text="Contact")
        self.SuppTable.heading("Description",text="Description")
       
        self.SuppTable["show"]="headings"

        self.SuppTable.column("Supplier Invoice",width=100)
        self.SuppTable.column("Supplier Name",width=100)
        self.SuppTable.column("Contact",width=80)
        self.SuppTable.column("Description",width=100)

        self.SuppTable.pack(fill=BOTH,expand=1)
        self.SuppTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()

#____
    def add(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_SupInvoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where SupInvoice=?",(self.var_SupInvoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier Invoice is Already Assigned, Try A Different One",parent=self.root)
                else:
                    cur.execute("Insert into supplier(SupInvoice,SuppName,Contact,Address) values(?,?,?,?)",(
                                self.var_SupInvoice.get(),
                                self.var_SuppName.get(),
                                self.var_Contact.get(), 
                                self.txt_Address.get('1.0',END),
                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SuppTable.delete(*self.SuppTable.get_children())
            for row in rows:
                self.SuppTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def get_data(self,ev):
        f=self.SuppTable.focus()
        content=(self.SuppTable.item(f))
        row=content['values']
        print(row)
        self.var_SupInvoice.set(row[0])
        self.var_SuppName.set(row[1]),
        self.var_Contact.set(row[2]),
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[3]),

    def update(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_SupInvoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where SupInvoice=?",(self.var_SupInvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Invoice, Try A Different One",parent=self.root)
                else:
                    cur.execute("Update supplier set SuppName=?,Contact=?,Address=? where SupInvoice=?",(            
                                self.var_SuppName.get(),
                                self.var_Contact.get(),
                                self.txt_Address.get('1.0',END),
                                self.var_SupInvoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")        
    
    def delete(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_SupInvoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where SupInvoice=?",(self.var_SupInvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Invoice, Try A Different One",parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete?",parent=self.root)
                    if op==True:
                        
                        cur.execute("delete from supplier where SupInvoice=?",(self.var_SupInvoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Delted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")        
    
    def clear(self):
        self.var_SuppName.set("")
        self.var_Contact.set("")
        self.txt_Address.delete("1.0",END)
        self.var_SupInvoice.set("")  
        self.var_SearchTxt.set("")  
        self.show()                                                                                                             
                        

    def search(self):
        con=sqlite3.connect(database=r"project.db")
        cur=con.cursor()
        try:
            if self.var_SearchBy.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            else:
                cur.execute("Select * from supplier where SupInvoice=?",(self.var_SearchTxt.get(),))
                row=cur.fetchone()
                if row!=0:
                    self.SuppTable.delete(*self.SuppTable.get_children())
                    self.SuppTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

        
        



if __name__=="__main__":       
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()