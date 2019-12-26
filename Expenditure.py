import tkinter as tk
from tkinter import messagebox
import mysql.connector

def setup_DB():
    # Setup the database
    mydb = mysql.connector.connect(host="", user="",passwd = "", database = "") # Add details here
    mycursor = mydb.cursor()
    return(mydb, mycursor)

def init():
    # Create the expenditure window
    window = tk.Tk()
    window.geometry("500x400") # Set the size of the window
    window.title("Expenditure") # Set the title
    window.configure(background = 'black')
    return(window)

def setup_GUI(root):
    canvas1 = tk.Canvas(root, width = 500, height = 500, bg = "Black")
    # Place the entry boxes
    CreateTextEntryBoxes(root, canvas1)
    # Add text before the entry boxes 
    addText2EntryBoxes(root, canvas1)
    # Add button
    addButton(canvas1, root)

def CreateTextEntryBoxes(root, canvas1):
    # Create boxes to enter text in
    global entry1, entry2, entry3, entry4, entry5

    entry1 = tk.Entry (root) 
    canvas1.create_window(250, 40, window = entry1)
    canvas1.pack()

    entry2 = tk.Entry (root) 
    canvas1.create_window(250, 80, window = entry2)
    canvas1.pack()

    entry3 = tk.Entry (root) 
    canvas1.create_window(250, 120, window = entry3)
    canvas1.pack()

    entry4 = tk.Entry (root) 
    canvas1.create_window(250, 160, window = entry4)
    canvas1.pack()

    entry5 = tk.Entry (root) 
    canvas1.create_window(250, 200, window = entry5)
    canvas1.pack()

def addText2EntryBoxes(root, canvas1):
    # Label the text entry boxes
    label1 = tk.Label(root, text="Date: ", fg = "white", bg = "black")
    label1.config(font=('helvetica', 10))
    canvas1.create_window(160, 40, window=label1)

    label2 = tk.Label(root, text="Month:" , fg = "white", bg = "black")
    label2.config(font=('helvetica', 10))
    canvas1.create_window(160, 80, window=label2)

    label3 = tk.Label(root, text="Year: ", fg = "white", bg = "black")
    label3.config(font=('helvetica', 10))
    canvas1.create_window(160, 120, window=label3)

    label3 = tk.Label(root, text="Amount: ", fg = "white", bg = "black")
    label3.config(font=('helvetica', 10))
    canvas1.create_window(160, 160, window=label3)

    label3 = tk.Label(root, text="Reason: ", fg = "white", bg = "black")
    label3.config(font=('helvetica', 10))
    canvas1.create_window(160, 200, window=label3)

def addButton(canvas1, root):
    # Add buttons to perform functions
    button1 = tk.Button(text = "Add the data to the database", bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'), command = confirmation)
    canvas1.create_window(250, 250, window = button1)

    button2 = tk.Button(text = "Get Monthly Data", bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'), command = getMonthlyData)
    canvas1.create_window(250, 300, window = button2)

    button3 = tk.Button(text = "Close the window", bg = 'brown', fg = 'white', font = ('helvetica', 9, 'bold'), command = root.destroy)
    canvas1.create_window(250, 350, window = button3)

def detailsFunc():
    # Close the window if it is present and get the details from the text boxes
    global window_conf
    try:
        window_conf.destroy()
    except:
        pass
    year, month, date, amount, reason = getExpenditureDetails()
    SQL_Entry(year, month, date, amount, reason)

    print("Data Added")

def confirmation():
    # Send a confirmation message to add data to the database
    global  window_conf
    window_conf = tk.Tk()
    window_conf.geometry("400x250") # Set the size of the window
    window_conf.title("Confirmation") # Set the title
    window_conf.configure(background = 'black')

    canvas1 = tk.Canvas(window_conf, width = 400, height = 250, bg = "black")
    canvas1.pack()

    text = "Confirm the Data Entry"
    label1 = tk.Label(window_conf, text= text, fg = "white", bg = "black")
    label1.config(font = ('arial', 20))
    canvas1.create_window(200, 40, window=label1)
    canvas1.pack()

    button2 = tk.Button(window_conf, text = "Yes", bg = 'green', fg = 'white', font = ('helvetica', 13, 'bold'), command = detailsFunc)
    canvas1.create_window(160, 150, window = button2)
    canvas1.pack()

    button2 = tk.Button(window_conf, text = "No", bg = 'red', fg = 'white', font = ('helvetica', 13, 'bold'), command = window_conf.destroy)
    canvas1.create_window(240, 150, window = button2)
    canvas1.pack()

def getMonthlyData():
    # Get the monthy income
    year = entry3.get()
    month = entry2.get()
    sql = "SELECT amount FROM Expenditure3 WHERE Year = " + year + " AND Month = " + month

    try:
        mycursor.execute(sql)
        result = mycursor.fetchall()

    except:
        messagebox.showerror("Error", "Enter month and year correctly")
        return

    sum = 0
    for i in result:
        sum += i[0]
    
    createAndDeleteWindow(sum)

def createAndDeleteWindow(sum):
    disp_window = tk.Tk()
    disp_window.geometry("400x300") # Set the size of the window
    disp_window.title("Expenditure") # Set the title
    disp_window.configure(background = 'black')

    canvas1 = tk.Canvas(disp_window, width = 400, height = 300, bg = "black")
    canvas1.pack()

    button2 = tk.Button(disp_window, text = "Close", bg = 'brown', fg = 'white', font = ('helvetica', 12, 'bold'), command = disp_window.destroy)
    canvas1.create_window(200, 200, window = button2)
    canvas1.pack()

    month = entry2.get()
    year = entry3.get()

    text = "The Expenditure for " + month + "/" + year + " is " + str(sum) 
    label1 = tk.Label(disp_window, text= text, fg = "white", bg = "black")
    label1.config(font=('arial', 14))
    canvas1.create_window(180, 40, window=label1)
    canvas1.pack()
    #window.mainloop()

def SQL_Entry(year, month, date, amount, reason):
    # Write the SQL Query
    sql = """INSERT INTO Expenditure3 VALUES (DEFAULT, %s, %s, %s, %s, %s)"""
    val = (year, month, date, amount, reason)
    mycursor.execute(sql, val)

    mydb.commit()

def getExpenditureDetails():
    # Get amount and reason of the transaction
    day = entry1.get()
    month = entry2.get()
    year = entry3.get()

    amount = entry4.get()
    reason = entry5.get()

    return(year, month, day, amount, reason)
 
if __name__ == "__main__":
    mydb, mycursor = setup_DB()
    window = init()
    setup_GUI(window)
    window.mainloop()
