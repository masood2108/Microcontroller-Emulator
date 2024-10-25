class Task:
    def __init__(self, task_id, execution_time, priority):
        self.task_id = task_id
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.priority = priority
        self.state = "ready"

    def run(self, time_slice):
        if self.remaining_time > 0:
            time_to_run = min(time_slice, self.remaining_time)
            self.remaining_time -= time_to_run
            print(f"Task {self.task_id} running for {time_to_run} seconds...")
            return time_to_run
        return 0
