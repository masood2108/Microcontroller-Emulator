import queue

class RTOSTask(Task):
    def __init__(self, task_id, execution_time, priority):
        super().__init__(task_id, execution_time, priority)
        self.message_queue = queue.Queue()

    def send_message(self, msg):
        self.message_queue.put(msg)

    def receive_message(self):
        if not self.message_queue.empty():
            return self.message_queue.get()
        return None

class RTOSEmulator:
    def __init__(self, tasks):
        self.tasks = tasks
        self.mutex = threading.Lock()

    def run(self):
        while any(task.remaining_time > 0 for task in self.tasks):
            for task in self.tasks:
                if task.remaining_time > 0:
                    self.mutex.acquire()
                    try:
                        task.run(1)
                    finally:
                        self.mutex.release()
                    time.sleep(1)
