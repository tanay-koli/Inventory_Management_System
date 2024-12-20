import sqlite3 
def create_db():
    con=sqlite3.connect(database=r"project.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(EmpID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,DOB text,DOJ text,Password text,UserType text,Address text,Salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(SupInvoice INTEGER PRIMARY KEY AUTOINCREMENT,SuppName text,Contact text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(CatID INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,Name text,price text,Qty text,status text)")
    con.commit()


create_db()