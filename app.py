import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Error", "Please enter a task!")
    else:
        with open('task.txt', 'a') as file:
            file.write(f"{task}\n")
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")

def remove_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Error", "Please enter a task!")
    else:
        tasks = []
        with open('task.txt', 'r') as file:
            tasks = file.readlines()
        with open('task.txt', 'w') as file:
            removed = False
            for t in tasks:
                if t.strip() == task and not removed:
                    removed = True
                else:
                    file.write(t)
        task_entry.delete(0, tk.END)
        if removed:
            messagebox.showinfo("Success", "Task removed successfully!")
        else:
            messagebox.showwarning("Error", "Task not found!")

def view_tasks():
    with open('task.txt', 'r') as read:
        results = read.readlines()
        tasks_text.delete(1.0, tk.END)
        for result in results:
            tasks_text.insert(tk.END, result)

def mark_task_complete():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Error", "Please enter a task!")
    else:
        tasks = []
        with open('task.txt', 'r') as file:
            tasks = file.readlines()
        with open('task.txt', 'w') as file:
            marked = False
            for t in tasks:
                if t.strip() == task and not marked:
                    file.write(f"[COMPLETE] {t}")
                    marked = True
                else:
                    file.write(t)
        task_entry.delete(0, tk.END)
        if marked:
            messagebox.showinfo("Success", "Task marked as complete!")
        else:
            messagebox.showwarning("Error", "Task not found!")

def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Task Manager")

# Set light blue background color
root.configure(bg="#BDE4F5")

# Create and place widgets
welcome_label = tk.Label(root, text="Welcome to the task manager:", bg="#BDE4F5")
welcome_label.pack()

task_frame = tk.Frame(root, bg="#BDE4F5")
task_frame.pack()

task_label = tk.Label(task_frame, text="Task:", bg="#BDE4F5")
task_label.grid(row=0, column=0)

task_entry = tk.Entry(task_frame)
task_entry.grid(row=0, column=1)

add_task_button = tk.Button(task_frame, text="Add Task", command=add_task)
add_task_button.grid(row=0, column=2, padx=10)

remove_task_button = tk.Button(task_frame, text="Remove Task", command=remove_task)
remove_task_button.grid(row=0, column=3, padx=10)

mark_task_complete_button = tk.Button(task_frame, text="Mark Task as Complete", command=mark_task_complete)
mark_task_complete_button.grid(row=0, column=4, padx=10)

task_added_label = tk.Label(root, text="", bg="#BDE4F5")
task_added_label.pack()

task_removed_label = tk.Label(root, text="", bg="#BDE4F5")
task_removed_label.pack()

task_marked_label = tk.Label(root, text="", bg="#BDE4F5")
task_marked_label.pack()

view_tasks_button = tk.Button(root, text="View My Tasks", command=view_tasks)
view_tasks_button.pack()

tasks_text = tk.Text(root, height=10, width=50)
tasks_text.pack()

exit_button = tk.Button(root, text="Exit Program", command=exit_program)
exit_button.pack()

root.mainloop()
