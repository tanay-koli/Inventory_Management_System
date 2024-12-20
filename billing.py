from cProfile import label
from cgitb import text
from http.client import EXPECTATION_FAILED
from operator import index
import sqlite3
from sqlite3 import Cursor
from sys import float_repr_style
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tokenize import String
from tkinter import ttk
from turtle import width
from unittest import result
from PIL import Image, ImageTk
import time
import os
import tempfile


class BI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x735+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.cart_list = []
        self.chk_print = 0
        # title
        self.icon_title = Image.open("images\logo1.jpg")
        self.icon_title = self.icon_title.resize((150, 125), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, 'bold'), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # button_logout
        button_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 17, "bold"),
                               bg="white", bd=2, cursor='hand2').place(x=1150, y=10, height=50, width=150)

        # clock
        self.lbl_clock = Label(self.root, text="Welcome To Inventory Management System\t\t Date : DD-MM-YYYY\t\t Time : HH:MM:SS ",
                               font=("times new roman", 15), bg="black", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # product frame
        ProductFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame.place(x=10, y=110, width=410, height=550)

        pTitle = Label(ProductFrame, text="All Products", font=(
            "goudy old style", 20, "bold"), bg="black", fg="white").pack(side=TOP, fill=X)

        

        ProductFrame3 = Frame(ProductFrame, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=50, width=398, height=500)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=(
            "PID", "Name", "Price", "QTY", "Status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("PID", text="PID No.")
        self.product_Table.heading("Name", text="Name")
        self.product_Table.heading("Price", text="Price")
        self.product_Table.heading("QTY", text="QTY")
        self.product_Table.heading("Status", text="Status")
        self.product_Table["show"] = "headings"

        self.product_Table.column("PID", width=50)
        self.product_Table.column("Name", width=100)
        self.product_Table.column("Price", width=80)
        self.product_Table.column("QTY", width=50)
        self.product_Table.column("Status", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind('<ButtonRelease-1>', self.get_data)

        lbl_note = Label(ProductFrame3, text="Note: 'Enter 0 Quantity to remove product from the Cart'", font=(
            "goudy old style", 10), bg="white", fg="red").pack(side=BOTTOM, fill=Y)

        # Customer Frame

        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)

        cTitle = Label(CustomerFrame, text="Customer Details", font=(
            "goudy old style", 15), bg="Lightgray").pack(side=TOP, fill=X)
        lbl_search = Label(CustomerFrame, text="Name", font=(
            "times new roman", 15,), bg="white").place(x=2, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=(
            "times new roman", 15), bg="light yellow", cursor="hand2").place(x=60, y=35, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=(
            "times new roman", 15,), bg="white").place(x=260, y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=(
            "times new roman", 15), bg="light yellow", cursor="hand2").place(x=370, y=35, width=140)

        calc_cartFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        calc_cartFrame.place(x=420, y=190, width=530, height=360)

        self.var_calc_input = StringVar()
        CalcFrame = Frame(calc_cartFrame, bd=4, relief=RIDGE, bg="white")
        CalcFrame.place(x=5, y=10, width=268, height=340)

        self.txt_calc_input = Entry(CalcFrame, textvariable=self.var_calc_input, font=(
            "times new roman", 15, "bold"), width=22, bd=10, relief=GROOVE, justify=RIGHT)
        self.txt_calc_input.grid(row=0, columnspan=4)

        btn_7 = Button(CalcFrame, text=7, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            7), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=0)
        btn_8 = Button(CalcFrame, text=8, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            8), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=1)
        btn_9 = Button(CalcFrame, text=9, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            9), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=2)
        btn_sum = Button(CalcFrame, text='+', font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            '+'), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=3)

        btn_4 = Button(CalcFrame, text=4, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            4), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=0)
        btn_5 = Button(CalcFrame, text=5, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            5), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=1)
        btn_6 = Button(CalcFrame, text=6, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            6), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=2)
        btn_subtract = Button(CalcFrame, text='-', font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            '-'), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=3)

        btn_1 = Button(CalcFrame, text=1, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            1), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=0)
        btn_2 = Button(CalcFrame, text=2, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            2), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=1)
        btn_3 = Button(CalcFrame, text=3, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            3), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=2)
        btn_multiply = Button(CalcFrame, text='*', font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            '*'), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=3)

        btn_0 = Button(CalcFrame, text=0, font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            0), bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=0)
        btn_c = Button(CalcFrame, text='C', font=('times new roman', 15, 'bold'), command=self.clear,
                       bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=1)
        btn_divide = Button(CalcFrame, text='/', font=('times new roman', 15, 'bold'), command=lambda: self.get_input(
            '/'), bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=2)
        btn_isto = Button(CalcFrame, text='=', font=('times new roman', 15, 'bold'), command=self.perform,
                          bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=3)

        cart_Frame = Frame(calc_cartFrame, bd=3, relief=RIDGE)
        cart_Frame.place(x=280, y=8, width=245, height=342)
        self.cartTitle = Label(cart_Frame, text="Cart \t Total Product: [0]", font=(
            "goudy old style", 15), bg="Lightgray")
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.cartTable = ttk.Treeview(cart_Frame, columns=(
            "PID", "Name", "Price", "QTY"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        self.cartTable.heading("PID", text="PID")
        self.cartTable.heading("Name", text="Name")
        self.cartTable.heading("Price", text="Price")
        self.cartTable.heading("QTY", text="QTY")

        self.cartTable["show"] = "headings"

        self.cartTable.column("PID", width=40)
        self.cartTable.column("Name", width=90)
        self.cartTable.column("Price", width=90)
        self.cartTable.column("QTY", width=40)

        self.cartTable.pack(fill=BOTH, expand=1)
        self.cartTable.bind('<ButtonRelease-1>', self.get_data_cart)

        # ADD CART BUTTON
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_QTY = StringVar()
        self.var_Price = StringVar()
        self.var_Stock = StringVar()

        Add_calc_cartFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_calc_cartFrame.place(x=420, y=550, width=530, height=110)

        lbl_p_name = Label(Add_calc_cartFrame, text="Product Name", font=(
            "Times new roman", 15), bg="white").place(x=5, y=5)
        txt_p_name = Entry(Add_calc_cartFrame, textvariable=self.var_pname, font=(
            "Times new roman", 15), bg="light yellow").place(x=5, y=35, width=190, height=22)

        lbl_p_price = Label(Add_calc_cartFrame, text="Product Price", font=(
            "Times new roman", 15), bg="white").place(x=210, y=5)
        txt_p_price = Entry(Add_calc_cartFrame, textvariable=self.var_Price, font=(
            "Times new roman", 15), bg="light yellow").place(x=210, y=35, width=150, height=22)

        lbl_p_qty = Label(Add_calc_cartFrame, text="Quantity", font=(
            "Times new roman", 15), bg="white").place(x=380, y=5)
        txt_p_qty = Entry(Add_calc_cartFrame, textvariable=self.var_QTY, font=(
            "Times new roman", 15), bg="light yellow").place(x=380, y=35, width=120, height=22)

        self.lbl_p_stock = Label(Add_calc_cartFrame, text="In Stock", font=(
            "Times new roman", 15), bg="white")
        self.lbl_p_stock.place(x=5, y=70)

        btn_clear_cart = Button(Add_calc_cartFrame, text="Clear", command=self.clear_cart, font=(
            "times new roman", 15, 'bold'), bg="lightgray", cursor="hand2").place(x=180, y=70, width=150, height=30)

        btn_add_cart = Button(Add_calc_cartFrame, text="Add/Update Cart", command=self.add_update_cart, font=(
            "times new roman", 15, 'bold'), bg="Orange", cursor="hand2").place(x=340, y=70, width=180, height=30)

        billframe1 = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billframe1.place(x=958, y=110, width=430, height=410)
        bTitle = Label(billframe1, text="Customer Bill Area", font=(
            "goudy old style", 20, "bold"), bg="#f44336", fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billframe1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area1 = Text(billframe1, yscrollcommand=scrolly.set)
        self.txt_bill_area1.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area1.yview)

        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white').place(
            x=958, y=520, width=430, height=140)

        self.lbl_amount = Label(billMenuFrame, text='Bill Amount\n0', font=(
            "goudy old style", 15, 'bold'), bg="Blue", fg='white')
        self.lbl_amount.place(x=963, y=525, width=120, height=70)
        self.lbl_discount = Label(billMenuFrame, text='Discount\n[5%]', font=(
            "goudy old style", 15, 'bold'), bg="Green", fg='white')
        self.lbl_discount.place(x=1100, y=525, width=120, height=70)
        self.lbl_net_pay = Label(billMenuFrame, text='Net Pay\n0', font=(
            "goudy old style", 15, 'bold'), bg="Orange", fg='white')
        self.lbl_net_pay.place(x=1230, y=525, width=140, height=70)

        btn_amount = Button(billMenuFrame, text='Print', command=self.print_bill, font=("goudy old style", 15, 'bold'),
                            bg="lightYellow", fg='gray', cursor='hand2').place(x=963, y=595, width=120, height=60)
        btn_clear_all = Button(billMenuFrame, text='Clear All', command=self.clear_all, font=(
            "goudy old style", 15, 'bold'), bg="red", fg='white', cursor='hand2').place(x=1100, y=595, width=120, height=60)
        btn_generate = Button(billMenuFrame, text='Generate Bill', command=self.generate_bill, font=(
            "goudy old style", 15, 'bold'), bg="Light Green", fg='white', cursor='hand2').place(x=1230, y=595, width=140, height=60)

####FOOOOOOOTTTTTEEEEERRRRRR#######
        # footer
        lbl_footer = Label(self.root, text=" IMS - Inventory Management System ", font=(
            "times new roman", 15, 'bold'), bg="#010c48", fg="white").pack(side=BOTTOM, fill=X)

        self.show()
        self.date_time()

    def get_input(self, num):
        xnum = self.var_calc_input.get()+str(num)
        self.var_calc_input.set(xnum)

    def clear(self):
        self.var_calc_input.set('')

    def perform(self):
        result = self.var_calc_input.get()
        self.var_calc_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            # self.product_Table=ttk.Treeview(ProductFrame3,columns=("PID","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute(
                "Select pid,name,price,qty,status from product where status='Active' ")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

   

    def get_data(self, ev):
        f = self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_Price.set(row[2])
        self.lbl_p_stock.config(text=f'In Stock [{str(row[3])}]')
        self.var_Stock.set(row[4])
        self.var_QTY.set('1')

    def get_data_cart(self, ev):
        f = self.cartTable.focus()
        content = (self.cartTable.item(f))
        row = content['values']
        # pid,name,price,qty,status
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_Price.set(row[2])
        self.var_QTY.set(row[3])
        self.lbl_p_stock.config(text=f'In Stock [{int(row[4])}]')
        self.var_Stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror(
                'Error', 'Please select product from the list', parent=self.root)
        elif self.var_QTY.get() == '':
            messagebox.showerror(
                'Error', "Quantity is required", parent=self.root)
        elif (self.var_QTY.get()) > (self.var_Stock.get()):
            messagebox.showerror('error', "Invalid Quantity", parent=self.root)
        else:
            #price_cal=float( int(self.var_QTY.get())*float(self.var_Price.get()))
            # print(price_cal)
            price_cal = self.var_Price.get()
            # pid,name,price,qty,status
            cart_data = [self.var_pid.get(), self.var_pname.get(
            ), price_cal, self.var_QTY.get(), self.var_Stock.get()]

            # update cart
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno(
                    'Confirm', "Product Already present\nDo you want to update/remove from Cart list", parent=self.root)
                if op == True:
                    if self.var_QTY.get() == '0':
                        self.cart_list.pop(index_)
                    else:
                        # pid,name,price,qty,status
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3] = self.var_QTY.get()  # qty
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amount = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amount = self.bill_amount+(float(row[2])*int(row[3]))

        self.discount = (self.bill_amount*5)/100
        self.net_pay = self.bill_amount-self.discount
        self.lbl_amount.config(text=f'Bill Amount\n[{str(self.bill_amount)}]')
        self.lbl_net_pay.config(text=f'Net pay(Rs.)\n[{str(self.net_pay)}]')
        self.cartTitle.config(
            text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            # self.product_Table=ttk.Treeview(ProductFrame3,columns=("PID","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get() == '':
            messagebox.showerror(
                "Error", f'Customer Details are required', parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror(
                "error", f"Please Add Product in the cart!!", parent=self.root)
        else:
            # ======Bill Top======
            self.bill_top()
            # ======Bill Middle====
            self.bill_middle()
            # ======Bill Bottom=====
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area1.get('1.0', END))
            fp.close()
            messagebox.showinfo(
                "Saved", "Bill has been Generated", parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + \
            int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tXYZ-Inventory
\t Phone No. 98725***** , Mumbai-410208
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area1.delete('1.0', END)
        self.txt_bill_area1.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amount}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area1.insert(END, bill_bottom_temp)

    def bill_middle(self):
        for row in self.cart_list:
        # pid,name,price,qty,stock
            name=row[1]
            qty=row[3]
            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area1.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_Price.set('')
        self.var_QTY.set('')
        self.lbl_p_stock.config(text=f'In Stock')
        self.var_Stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area1.delete('1.0', END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0

    def date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m:%Y")
        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}", font=(
            "times new roman", 15), bg="black", fg="white")
        self.lbl_clock.after(200, self.date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo(
                'Print', 'Please wait while printing', parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area1.get(1.0, END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror(
                'Print', 'Please Generate bill to print the receipt', parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("login.py")


if __name__ == "__main__":
    root = Tk()
    obj = BI(root)
    root.mainloop()