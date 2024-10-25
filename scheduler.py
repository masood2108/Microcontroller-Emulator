import time
import threading

class RoundRobinScheduler:
    def __init__(self, tasks, time_slice):
        self.tasks = tasks
        self.time_slice = time_slice

    def run(self):
        while any(task.remaining_time > 0 for task in self.tasks):
            for task in self.tasks:
                if task.remaining_time > 0:
                    task.run(self.time_slice)
                    time.sleep(self.time_slice)

class PriorityScheduler:
    def __init__(self, tasks):
        self.tasks = sorted(tasks, key=lambda x: x.priority)

    def run(self):
        for task in self.tasks:
            while task.remaining_time > 0:
                task.run(1)
                time.sleep(1)
