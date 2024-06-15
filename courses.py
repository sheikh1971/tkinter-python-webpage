import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_python_details():
    details = """
    Python Programming Course:
    - Duration: 8 weeks
    - Cost: $200
    - Introduction to Python basics and advanced topics.
    - Hands-on projects and assignments.
    """
    messagebox.showinfo("Python Programming Details", details)

def show_web_dev_details():
    details = """
    Web Development Course:
    - Duration: 10 weeks
    - Cost: $250
    - Covers both frontend and backend technologies.
    - Build real-world projects.
    """
    messagebox.showinfo("Web Development Details", details)

# Add more functions like the ones above for other courses...

def show_course_details(course_name):
    if course_name == "Python Programming":
        show_python_details()
    elif course_name == "Web Development":
        show_web_dev_details()
    # Add conditions for other courses similarly...

def buy_course(course_name):
    print(f"Buy Now clicked for {course_name}")

root = tk.Tk()
root.title("IT Courses")
root.iconbitmap("computer.ico")
root.configure(bg="wheat")

style = ttk.Style()
style.configure("Custom.TFrame", background="azure")

frame = ttk.Frame(root, padding="20", style="Custom.TFrame")
frame.pack(padx=50, pady=30)

courses_info = [
    {"name": "Python Programming", "color": "#FF6B6B"},
    {"name": "Web Development", "color": "#6BFF6B"},
    {"name": "Data Science", "color": "#FFD700"},
    {"name": "Cloud Computing", "color": "#ADD8E6"},
    {"name": "Mobile App Development","color": "#FFC0CB"},
    {"name": "Networking Basics", "color": "#98FB98"},
    {"name": "Database", "color": "#98FB98"},
    {"name": "Software Testing", "color": "#6B6BFF"}
]

box_count = 0

for course in courses_info:
    if box_count % 3 == 0:
        row_frame = ttk.Frame(frame, style="Custom.TFrame")
        row_frame.pack(pady=10)

    course_frame = ttk.Frame(row_frame, padding="10", relief="raised", borderwidth=2, style="Custom.TFrame")
    course_frame.pack(padx=10, side=tk.LEFT)
    
    course_name_label = ttk.Label(course_frame, text=course['name'], font=("Arial", 16, "bold"), background="azure")
    course_name_label.pack(pady=(10, 5))
    
    btn_frame = ttk.Frame(course_frame, style="Custom.TFrame")
    btn_frame.pack(pady=10)
    
    details_btn = ttk.Button(btn_frame, text="Details", style="TButton", command=lambda c=course['name']: show_course_details(c))
    details_btn.pack(side=tk.LEFT, padx=5)
    
    buy_btn = ttk.Button(btn_frame, text="Buy Now", style="TButton", command=lambda c=course["name"]: buy_course(c))
    buy_btn.pack(side=tk.RIGHT, padx=5)

    box_count += 1

root.mainloop()
