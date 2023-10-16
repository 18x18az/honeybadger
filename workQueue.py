import queue
import threading

class FunctionQueue:
    def __init__(self):
        self.func_queue = queue.Queue()
        self.pause_event = threading.Event()
        self.worker_thread = threading.Thread(target=self.worker)
        self.worker_thread.daemon = True
        self.is_paused = False

    def add_function(self, func, *args, **kwargs):
        self.func_queue.put((func, args, kwargs))

    def start(self):
        self.worker_thread.start()

    def pause(self):
        self.is_paused = True
        self.pause_event.set()

    def unpause(self):
        self.is_paused = False
        self.pause_event.clear()

    def worker(self):
        while True:
            try:
                if self.is_paused:
                    self.pause_event.wait()

                func, args, kwargs = self.func_queue.get(timeout=1)
                func(*args, **kwargs)
                self.func_queue.task_done()
            except queue.Empty:
                continue

workQueue = FunctionQueue()

def add_function(func, *args, **kwargs):
    workQueue.add_function(func, *args, **kwargs)

def pause():
    workQueue.pause()

def unpause():
    workQueue.unpause()

workQueue.start()