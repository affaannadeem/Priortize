import tkinter as tk
from tkinter import messagebox

class PrioritizeApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Prioritize - To-Do List App")

        self.tasks = []

        # Frame for the task list
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box to add tasks
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Button to add task
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Button to prioritize task
        self.prioritize_task_button = tk.Button(self.root, text="Prioritize Task", command=self.prioritize_task)
        self.prioritize_task_button.pack(pady=5)

        # Button to remove task
        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def prioritize_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            self.tasks.insert(0, task)  # Move task to the top
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to prioritize.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "_main_":
    root = tk.Tk()
    app = PrioritizeApp(root)
    root.mainloop()