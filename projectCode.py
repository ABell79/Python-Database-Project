import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import simpledialog
import sqlite3 


# Function to insert data into the database
def create_database():
    conn = sqlite3.connect("compData.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE  IF NOT EXISTS comps (
                   id INTEGER PRIMARY KEY,
                   coName TEXT,
                   email TEXT,
                   phonNum TEXT,
                   conName TEXT,
                   availRes TEXT,
                   orgType TEXT,
                   other TEXT)''')
    conn.commit() #Commits the changes to the database
    conn.close()


#Displays the data in a treeview table
def display_table():
    root_table = Tk()
    root_table.title("Data Table")
    root_table.geometry("1000x500")
    


    #Creates Table
    tree = ttk.Treeview(root_table, column=("column0", "column1", "column2", "column3", "column4", "column5", "column6"))
    hsb = ttk.Scrollbar(root_table, orient="horizontal", command=tree.xview) 
    tree.configure(xscrollcommand=hsb.set)
    hsb.grid(column=0, row=8, sticky='ew')
    tree.heading("#1", text="Company Name")
    tree.heading("#2", text="Email")
    tree.heading("#3", text="Contact Number")
    tree.heading("#4", text="Contact Name")
    tree.heading("#5", text="Available Resources")
    tree.heading("#6", text="Organization Type")
    tree.heading("#7", text="Other")
    tree.grid(row=1, column=0, columnspan=2)

    #Connects to Db
    conn = sqlite3.connect("compData.db")
    cursor = conn.cursor()
    cursor.execute("SELECT coName, email, phonNum, conName, availRes, orgType, other FROM comps")  # Adjusted column names
    data = cursor.fetchall()
    for row in data:
        tree.insert("", END, values=row)
    conn.close()

    root_table.mainloop()

#Takes info and adds it to database
def insert_data():
    root_table = Tk()
    tree = ttk.Treeview(root_table, column=("column0", "column1", "column2", "column3", "column4", "column5", "column6"))
    coname = company_name_entry.get()
    email = email_name_entry.get()
    phonnum = phone_entry.get()
    conname = contact_name_entry.get()
    availres = resources_entry.get()
    orgtype = organization_type_entry.get()
    other = other_entry.get()

    if coname and email and phonnum and availres and conname and orgtype and other:
        conn = sqlite3.connect("compData.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comps (coName, email, phonNum, conName, availRes, orgType, other) VALUES (?,?,?,?,?,?,?)", (coname, email, phonnum, conname, availres, orgtype, other))
        cursor.execute("SELECT coName, email, phonNum, conName, availRes, orgType, other FROM comps")  # Adjusted column names
        data = cursor.fetchall()
        for row in data:
            print(row)
            tree.insert("", END, values=row)
        print(data)
        conn.commit()
        conn.close()



def delCon():
  #conn.close()
  company_name_entry.delete(0, "end")
  email_name_entry.delete(0, "end")
  phone_entry.delete(0, "end")
  contact_name_entry.delete(0, "end")
  resources_entry.delete(0, "end")
  organization_type_entry.delete(0, "end")
  other_entry.delete(0, "end")




# Create the add data window
def new_data():
    root = Tk()
    root.title("Add Data")
    root.geometry("1000x1000")

    #Calls the Create database function
    create_database()

    # Entry fields for company information with blank labels to space
    company_name_label = Label(root, text="Company Name:")
    company_name_label.grid(row=0,column=1)
    company_name_entry = Entry(root)
    company_name_entry.grid(row=0,column=2)

    blank_label1 = Label(root, text="")
    blank_label1.grid(row=1,column=1)

    #Takes Email Address
    email_name_label = Label(root, text="Email Address:")
    email_name_label.grid(row=2,column=1)
    email_name_entry = Entry(root)
    email_name_entry.grid(row=2,column=2)

    blank_label2 = Label(root, text="")
    blank_label2.grid(row=3,column=2)

    #Takes Phone number
    phone_label = Label(root, text="Phone Number:")
    phone_label.grid(row=4,column=1)
    phone_entry = Entry(root)
    phone_entry.grid(row=4,column=2)

    blank_label2 = Label(root, text="")
    blank_label2.grid(row=5,column=2)

    #Takes Contact Name
    contact_name_label = Label(root, text="Contact Name:")
    contact_name_label.grid(row=6,column=1)
    contact_name_entry = Entry(root)
    contact_name_entry.grid(row=6,column=2)

    blank_label2 = Label(root, text="")
    blank_label2.grid(row=7,column=2)

    #Takes Availible Resources
    resources_label = Label(root, text="Availible Resources:")
    resources_label.grid(row=8,column=1)
    resources_entry = Entry(root)
    resources_entry.grid(row=8,column=2)

    blank_label2 = Label(root, text="") 
    blank_label2.grid(row=9,column=2)

    #Takes Organization type
    organization_type_label = Label(root, text="Organization Type:")
    organization_type_label.grid(row=10,column=1)
    organization_type_entry = Entry(root)
    organization_type_entry.grid(row=10,column=2)

    blank_label2 = Label(root, text="")
    blank_label2.grid(row=11,column=2)

    other_label = Label(root, text="Other Information:")
    other_label.grid(row=12,column=1)
    other_entry = Entry(root)
    other_entry.grid(row=12,column=2)

    blank_label2 = Label(root, text="")
    blank_label2.grid(row=13,column=2)
    # Button to add information to the database
    add_button = Button(root, text="Add Info", command=insert_data)
    add_button.grid(row=15,column=1)



def fetch_data():
    # Connect to SQLite database
    connection = sqlite3.connect('compData.db')
    cursor = connection.cursor()

    # Execute a SELECT query to fetch data from the table
    cursor.execute("SELECT coname, email, phonnum, conname, availres, orgtype, other FROM comps")
    rows = cursor.fetchall()

    # Close the database connection
    connection.close()

    return rows


#create opening window
root = Tk()
root.title("Comoany Database")
root.geometry("500x500")

credit_label = Label(root, text="Company DataBase")
credit2_label = Label(root, text="Created by Aidan Bell")
credit_label.grid(row=2, column=1)
credit2_label.grid(row=3, column=1)
 





add_button = Button(root, text="Add New Data", command=new_data)
add_button.grid(row=15,column=1)

# Button to updata tabel
add_button = Button(root, text="Show Info", command=display_table)
add_button.grid(row=17,column=1)


# Run the main application loop
root.mainloop()