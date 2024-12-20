from ast import Delete
import sqlite3
from tkinter import *
from tkinter import font
from turtle import width
from webbrowser import get
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()
        # All Variables
        self.var_SearchBy = StringVar()
        self.var_SearchTxt = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_Qty = StringVar()
        self.var_status = StringVar()
        self.fetch_cat_sup()
        
        #Product Frame
        product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        product_Frame.place(x=10, y=10, width=450, height=480)

        # title
        title = Label(product_Frame, text=" Manage Product Details", font=(
            "goudy old style", 18, "bold"), bg="Dark Blue", fg="White").pack(side=TOP, fill=X)

        # column 1
        lbl_cat = Label(product_Frame, text="Category", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=60)
        lbl_sup = Label(product_Frame, text="Supplier", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=110)
        lbl_pn = Label(product_Frame, text="Name", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=210)
        lbl_Qty = Label(product_Frame, text="Quantity", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=310)

        # column 2
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list,
                               state="readonly", justify=CENTER, font=("goudy old style", 15, 'bold'))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list,
                               state="readonly", justify=CENTER, font=("goudy old style", 15, 'bold'))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=(
            "goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=(
            "goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=210, width=200)
        txt_Qty = Entry(product_Frame, textvariable=self.var_Qty, font=(
            "goudy old style", 15, 'bold'), bg='lightyellow').place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=(
            "Active", "Inactive"), state="readonly", justify=CENTER, font=("goudy old style", 15, 'bold'))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        # button
        btn_add = Button(product_Frame, text="Save", command=self.add, font=(
            "goudy old style", 15, 'bold'), bg="lightgreen", fg="black", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=(
            "goudy old style", 15, 'bold'), bg="lightblue", fg="black", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=(
            "goudy old style", 15, 'bold'), bg="red", fg="black", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=(
            "goudy old style", 15, 'bold'), bg="grey", fg="black", cursor="hand2").place(x=340, y=400, width=100, height=40)

        # searchframe
        SearchFrame = LabelFrame(self.root, text="Search Product", font=(
            "goudy old style", 12, 'bold'), bd=3, relief=RIDGE, bg="white")
        SearchFrame.place(x=480, y=10, width=600, height=80)

        # options
        cmb_searchbox = ttk.Combobox(SearchFrame, textvariable=self.var_SearchBy, values=(
            "Select", "Category", "Supplier", "Name"), state="readonly", justify=CENTER, font=("goudy old style", 15, 'bold'))
        cmb_searchbox.place(x=10, y=10, width=180)
        cmb_searchbox.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_SearchTxt, font=(
            "goudy old style", 15, 'bold'), bg="silver").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=(
            "goudy old style", 15, 'bold'), bg="yellow green", fg="black", cursor="hand2").place(x=430, y=7, width=130, height=30)

        # Product Details
        p_Frame = Frame(self.root, bd=4, relief=RIDGE)
        p_Frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_Frame, orient=VERTICAL)
        scrollx = Scrollbar(p_Frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_Frame, columns=(
            "pid","Supplier","Category", "Name", "price", "Qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid", text="Product ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("Name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("Qty", text="Qty")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=100)
        self.product_table.column("Name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("Qty", width=100)
        self.product_table.column("status", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind('<ButtonRelease-1>', self.get_data)
        self.show()


# __________

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            cur.execute("Select Name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("Select SuppName from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")  


    def add(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_sup.get() == "Empty" or self.var_name.get() == "":
                messagebox.showerror(
                    "Error", "All Fields are Required", parent=self.root)
            else:
                cur.execute("Select * from product where Name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror(
                        "Error", "Product already present, Try A Different One", parent=self.root)
                else:
                    cur.execute("Insert into product(Category, Supplier, Name,price, Qty, status) values(?,?,?,?,?,?)", (
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_Qty.get(),
                                self.var_status.get(),
                                ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Product Added Sucessfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            cur.execute("Select * from product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_Qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", "Please Select Product from the list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Product, Try A Different One", parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,Name=?,price=?,Qty=?,status=? where pid=?", (
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_Qty.get(),
                                self.var_status.get(),
                                self.var_pid.get()
                                ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Product Updated Sucessfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", "Select Product from the list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Product, Try A Different One", parent=self.root)

                else:
                    op = messagebox.askyesno(
                            "Confirm", "Do You Really Want To Delete?", parent=self.root)
                    if op == True:
                        cur.execute(
                            "delete from product where pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_Qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
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
                cur.execute("Select * from product where "+self.var_SearchBy.get()+" LIKE '%"+self.var_SearchTxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
