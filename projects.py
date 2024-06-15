import tkinter as tk
from tkinter import ttk
import sqlite3
import os

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
    # Destroy the login window
    root.destroy()

    # Create a new window for the student portal
    student_portal = tk.Tk()
    student_portal.title("Student Portal")

    # Add a purpose label
    ttk.Label(student_portal, text="Welcome to the Student Portal! \nThese projects are the success of our students.\nThe students who will spend their quality time with us in these courses \ncan make or see their own works like that.\nChoose a project to explore:", font=("Times New Roman", 24, "bold")).pack(pady=120)

    # Create a style for the buttons
    button_style = ttk.Style()
    button_style.configure("Custom.TButton", 
                           background="#2F4F4F", 
                           foreground="green", 
                           font=("Arial", 16, "bold"),  
                           padding=10, 
                           relief="flat", 
                           borderwidth=0, 
                           shadow=True)

    # Create the buttons with the customized style
    ttk.Button(student_portal, text="Game project", command=open_brickbreak, style="Custom.TButton").pack(pady=30)
    ttk.Button(student_portal, text="Magic project", command=open_ninjacloth, style="Custom.TButton").pack(pady=30)

    # Start the Tkinter event loop for the student portal
    student_portal.mainloop()

def open_brickbreak():
    os.system('python brickbreak.py')

def open_ninjacloth():
    os.system('python ninjacloth.py')

# Create the main login window
root = tk.Tk()
root.title("Login Page")
root.geometry("1400x700")
root.iconbitmap("computer.ico")
style = ttk.Style(root)
style.configure("TButton", foreground="green", background="black", font=("Arial", 12, "bold"), padding=10, relief="flat", borderwidth=0)

# Set the background color of the login page to wheat
root.configure(bg="wheat")

# Variables to store username and password
username_var = tk.StringVar()
password_var = tk.StringVar()

# Create and pack a frame
frame = ttk.Frame(root, padding="100", style="TFrame")
frame.grid(row=0, column=0, padx=300, pady=150)

# Create and pack labels, entry widgets, and buttons
ttk.Label(frame, text="Username:", style="TLabel").grid(row=0, column=0, sticky="w")
username_entry = ttk.Entry(frame, textvariable=username_var, font=("Arial", 14))
username_entry.grid(row=0, column=1, pady=(0, 10))

ttk.Label(frame, text="Password:", style="TLabel").grid(row=1, column=0, sticky="w")
password_entry = ttk.Entry(frame, textvariable=password_var, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1, pady=(0, 10))

login_button = ttk.Button(frame, text="Login", command=validate_login, style="TButton")
login_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

status_label = ttk.Label(frame, text="", foreground="black")
status_label.grid(row=3, column=0, columnspan=2)

# Start the Tkinter event loop for the login window
root.mainloop()
