# Задание 1

import sqlite3
import tkinter as tk


conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                sale_id INTEGER PRIMARY KEY,
                salesman_id INTEGER,
                customer_id INTEGER,
                amount REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Salesmen (
                salesman_id INTEGER PRIMARY KEY,
                name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT)''')


cursor.execute("INSERT INTO Salesmen (name) VALUES ('John Doe')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Jane Smith')")
cursor.execute("INSERT INTO Sales (salesman_id, customer_id, amount) VALUES (1, 1, 1000.0)")

conn.commit()


root = tk.Tk()
root.title("Sales Database App")


def display_all_sales():
    cursor.execute("SELECT * FROM Sales")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


menu = tk.Menu(root)
root.config(menu=menu)

reports_menu = tk.Menu(menu)
menu.add_cascade(label="Reports", menu=reports_menu)
reports_menu.add_command(label="Display All Sales", command=display_all_sales)

root.mainloop()

conn.close()


# Задание 2

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                sale_id INTEGER PRIMARY KEY,
                salesman_id INTEGER,
                customer_id INTEGER,
                amount REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Salesmen (
                salesman_id INTEGER PRIMARY KEY,
                name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT)''')

cursor.execute("INSERT INTO Salesmen (name) VALUES ('John Doe')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Jane Smith')")
cursor.execute("INSERT INTO Sales (salesman_id, customer_id, amount) VALUES (1, 1, 1000.0)")

conn.commit()

root = tk.Tk()
root.title("Sales Database App")


def display_all_sales():
    cursor.execute("SELECT * FROM Sales")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def insert_data(table_name):
    if table_name in ['Sales', 'Salesmen', 'Customers']:
        pass


def update_data(table_name):
    if table_name in ['Sales', 'Salesmen', 'Customers']:
        pass


def delete_data(table_name):
    if table_name in ['Sales', 'Salesmen', 'Customers']:
        pass


menu = tk.Menu(root)
root.config(menu=menu)

reports_menu = tk.Menu(menu)
menu.add_cascade(label="Reports", menu=reports_menu)
reports_menu.add_command(label="Display All Sales", command=display_all_sales)

data_menu = tk.Menu(menu)
menu.add_cascade(label="Data Operations", menu=data_menu)
data_menu.add_command(label="Insert Data into Sales", command=lambda: insert_data('Sales'))
data_menu.add_command(label="Insert Data into Salesmen", command=lambda: insert_data('Salesmen'))
data_menu.add_command(label="Insert Data into Customers", command=lambda: insert_data('Customers'))

data_menu.add_command(label="Update Data in Sales", command=lambda: update_data('Sales'))
data_menu.add_command(label="Update Data in Salesmen", command=lambda: update_data('Salesmen'))
data_menu.add_command(label="Update Data in Customers", command=lambda: update_data('Customers'))

data_menu.add_command(label="Delete Data from Sales", command=lambda: delete_data('Sales'))
data_menu.add_command(label="Delete Data from Salesmen", command=lambda: delete_data('Salesmen'))
data_menu.add_command(label="Delete Data from Customers", command=lambda: delete_data('Customers'))

root.mainloop()

conn.close()

# Задание 3

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                sale_id INTEGER PRIMARY KEY,
                salesman_id INTEGER,
                customer_id INTEGER,
                amount REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Salesmen (
                salesman_id INTEGER PRIMARY KEY,
                name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT)''')

cursor.execute("INSERT INTO Salesmen (name) VALUES ('John Doe')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Jane Smith')")
cursor.execute("INSERT INTO Sales (salesman_id, customer_id, amount) VALUES (1, 1, 1000.0)")

conn.commit()

root = tk.Tk()
root.title("Sales Database App")


def display_all_sales():
    cursor.execute("SELECT * FROM Sales")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def save_to_file(data):
    file_path = "results.txt"
    with open(file_path, 'w') as file:
        for line in data:
            file.write(str(line) + '\n')
        print("Results saved to file:", file_path)


menu = tk.Menu(root)
root.config(menu=menu)

reports_menu = tk.Menu(menu)
menu.add_cascade(label="Reports", menu=reports_menu)
reports_menu.add_command(label="Display All Sales", command=display_all_sales)

data_menu = tk.Menu(menu)
menu.add_cascade(label="Data Operations", menu=data_menu)

data_menu.add_command(label="Save Filtered Data to File", command=lambda: save_to_file(["Filtered data 1", "Filtered data 2"]))

root.mainloop()

conn.close()

