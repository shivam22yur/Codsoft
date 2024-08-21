import tkinter as tk
from tkinter import messagebox

class ToDoListApp:

    def __init__(self, master):

        self.master = master

        self.master.title("To-Do List App")

        self.tasks = []

        # Entry widget to input new tasks
        self.task_entry = tk.Entry(master, width=60, bg='lightblue')
        self.task_entry.grid(row=0, column=0, padx=15, pady=15, columnspan=4)

        # Button to add a new task
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg='green', fg='white')
        self.add_button.grid(row=0, column=2, padx=5, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=50, bg='lightgrey')
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Button to delete selected task
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg='red', fg='white')
        self.remove_button.grid(row=1, column=2, padx=5, pady=10)

        # Button to mark task as completed
        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task, bg='yellow')
        self.complete_button.grid(row=2, column=0, padx=5, pady=10)

        # Button to update selected task
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg='purple', fg='white')
        self.update_button.grid(row=2, column=1, padx=5, pady=10)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.task_listbox.itemconfig(index, {"bg": "light green"})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[index]["task"] = new_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
