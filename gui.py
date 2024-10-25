import tkinter as tk
from tkinter import ttk
from scheduler import RoundRobinScheduler, PriorityScheduler
from task import Task
import threading

class TaskSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Microcontroller Emulator")
        self.tasks = []
        self.time_slice = 1
        self.selected_scheduler = None
        self.create_widgets()

    def create_widgets(self):
        self.task_frame = ttk.Frame(self.root)
        self.task_frame.pack()
        ttk.Label(self.task_frame, text="Task ID").grid(row=0, column=0)
        ttk.Label(self.task_frame, text="Execution Time").grid(row=0, column=1)
        ttk.Label(self.task_frame, text="Priority").grid(row=0, column=2)

        self.task_id_entry = ttk.Entry(self.task_frame)
        self.execution_time_entry = ttk.Entry(self.task_frame)
        self.priority_entry = ttk.Entry(self.task_frame)

        self.task_id_entry.grid(row=1, column=0)
        self.execution_time_entry.grid(row=1, column=1)
        self.priority_entry.grid(row=1, column=2)

        ttk.Button(self.task_frame, text="Add Task", command=self.add_task).grid(row=1, column=3)
        self.scheduler_var = tk.StringVar(value="RoundRobin")
        ttk.Radiobutton(self.root, text="Round Robin", variable=self.scheduler_var, value="RoundRobin").pack()
        ttk.Radiobutton(self.root, text="Priority", variable=self.scheduler_var, value="Priority").pack()

        ttk.Button(self.root, text="Start Scheduling", command=self.start_scheduling).pack()


        self.output_text = tk.Text(self.root, height=10)
        self.output_text.pack()

    def add_task(self):
        task_id = self.task_id_entry.get()
        execution_time = int(self.execution_time_entry.get())
        priority = int(self.priority_entry.get())

        task = Task(task_id, execution_time, priority)
        self.tasks.append(task)

        self.output_text.insert(tk.END, f"Added Task {task_id} - Time: {execution_time}, Priority: {priority}\n")

    def start_scheduling(self):
        if self.scheduler_var.get() == "RoundRobin":
            scheduler = RoundRobinScheduler(self.tasks, self.time_slice)
        else:
            scheduler = PriorityScheduler(self.tasks)

        threading.Thread(target=scheduler.run).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskSchedulerApp(root)
    root.mainloop()
