import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import hashlib
import os  # Import the os module

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if username exists
def check_username_exists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Function to register user into SQLite database
def register_user():
    username = username_entry.get()
    password = hash_password(password_entry.get())
    email = email_entry.get()
    phone = phone_entry.get()
    dob = dob_entry.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            dob TEXT NOT NULL
        );
    ''')

    if check_username_exists(username):
        messagebox.showerror("Error", "Invalid!")
        conn.close()
        return

    cursor.execute("INSERT INTO users (username, password, email, phone, dob) VALUES (?, ?, ?, ?, ?)", (username, password, email, phone, dob))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Registration Successful!")
    clear_entries()

# Function to log in user
def login_user():
    username = username_entry.get()
    password = hash_password(password_entry.get())

    if not check_username_exists(username):
        messagebox.showerror("Error", "Invalid!")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = cursor.fetchone()[0]
    conn.close()

    if password != stored_password:
        messagebox.showerror("Error", "Incorrect Password!")
        return

    messagebox.showinfo("Success", "Login Successful!")
    clear_entries()

# Function to clear entry fields
def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)

# Function to open the courses.py file
def open_projects_page():
    os.system("python projects.py")

# Function to open the login.py file
def open_login_page():
    os.system("python login.py")


# Main Tkinter window setup
root = tk.Tk()
root.title("IT Center Website")
root.geometry("1400x700")
root.configure(bg="cadetblue3")


try:
    root.iconbitmap('computer.ico')
except tk.TclError as e:
    print(f"Failed to load icon: {e}")

style = ttk.Style()
style.configure('Middle.TFrame', background='cadetblue4')

logo_label = ttk.Label(text="EAST DELTA IT Zone", font=("Times New Roman", 32, "bold"), background='black', foreground='white')
logo_label.pack(pady=20)

nav_frame = ttk.Frame(root)
nav_frame.pack(pady=(10, 10))

buttons = ["Homepage", "Contact", "Courses", "projects", "Student portal", "Log in", "Registration", "Gallery"]
for btn_text in buttons:
    if btn_text == "projects":
        btn = ttk.Button(nav_frame, text=btn_text, style="TButton", command=open_projects_page)
    elif btn_text == "Log in":
        btn = ttk.Button(nav_frame, text=btn_text, style="TButton", command=open_login_page)
    else:
        btn = ttk.Button(nav_frame, text=btn_text, style="TButton")
    btn.pack(side=tk.LEFT, padx=10,pady=10)

middle_frame = ttk.Frame(root, padding=10)
middle_frame.configure(style='Middle.TFrame')
middle_frame.pack(expand=True, fill=tk.BOTH)

ttk.Label(middle_frame, text="Registration/Login Form", font=("Arial", 20), background='cadetblue4', foreground='papayawhip').pack(pady=20)

username_label = ttk.Label(middle_frame, text="Username:", background='cadetblue4', foreground='papayawhip')
username_label.pack(pady=5)
username_entry = ttk.Entry(middle_frame, width=30)
username_entry.pack(pady=5)

password_label = ttk.Label(middle_frame, text="Password:", background='cadetblue4', foreground='papayawhip')
password_label.pack(pady=5)
password_entry = ttk.Entry(middle_frame, width=30, show="*")
password_entry.pack(pady=5)

email_label = ttk.Label(middle_frame, text="Email:", background='cadetblue4', foreground='papayawhip')
email_label.pack(pady=5)
email_entry = ttk.Entry(middle_frame, width=30)
email_entry.pack(pady=5)

phone_label = ttk.Label(middle_frame, text="Phone:", background='cadetblue4', foreground='papayawhip')
phone_label.pack(pady=5)
phone_entry = ttk.Entry(middle_frame, width=30)
phone_entry.pack(pady=5)

dob_label = ttk.Label(middle_frame, text="Date of Birth (YYYY-MM-DD):", background='cadetblue4', foreground='papayawhip')
dob_label.pack(pady=5)
dob_entry = ttk.Entry(middle_frame, width=30)
dob_entry.pack(pady=5)

register_button = ttk.Button(middle_frame, text="Register", command=register_user, style="TButton")
register_button.pack(pady=10)

login_button = ttk.Button(middle_frame, text="Login", command=login_user, style="TButton")
login_button.pack(pady=10)

footer_frame = ttk.Frame(root)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

combined_text = "Let's Code Together, Contact: +8801835674339, All rights reserved by Team 13"
footer_label = ttk.Label(footer_frame, text=combined_text, font=("Arial", 15, "italic"), foreground='black', background='', anchor=tk.CENTER)
footer_label.pack(pady=5)

root.mainloop()
