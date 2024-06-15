import tkinter as tk
from tkinter import ttk
import sqlite3
import os  # Import the os module
def validate_login():
    username = username_var.get()
    password = password_var.get()

    # Connect to the SQLite database
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Execute the query to check if the username and password exist in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user_data = cursor.fetchone()

    # Close the database connection
    connection.close()

    if user_data:
        status_label.config(text="Login successful!", foreground="green")
        open_student_portal()
    else:
        status_label.config(text="Invalid username or password.", foreground="red")
  

    
def open_student_portal():

    os.system("python courses.py")
   
 

    # Create a new window for the student portal
    student_portal = tk.Tk()
    student_portal.title("Student Portal")

    # Add widgets and functionalities to the student portal (customize as needed)
    ttk.Label(student_portal, text="Welcome to the Student Portal!").pack(pady=20)

    # Start the Tkinter event loop for the student portal
    student_portal.mainloop()

# Create the main login window
root = tk.Tk()
root.title("Login Page")
root.geometry("1400x700")
root.iconbitmap("computer.ico")
root.configure(bg="wheat")  # Set background color to wheat



# Variables to store username and password
username_var = tk.StringVar()
password_var = tk.StringVar()

# Create and pack a frame
frame = ttk.Frame(root, padding="200")
frame.grid(row=0, column=0, padx=300, pady=30)

# Create and pack labels, entry widgets, and buttons
ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky="w")
username_entry = ttk.Entry(frame, textvariable=username_var)
username_entry.grid(row=0, column=1, pady=(0, 10))

ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky="w")
password_entry = ttk.Entry(frame, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1, pady=(0, 10))

login_button = ttk.Button(frame, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

status_label = ttk.Label(frame, text="", foreground="black")
status_label.grid(row=3, column=0, columnspan=2)

# Start the Tkinter event loop for the login window
root.mainloop()
