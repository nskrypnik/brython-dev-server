import time
from multiprocessing import Queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

RESTART_QUEUE = Queue()


class SourceChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(event)
        RESTART_QUEUE.put_nowait(True)


def start_watchdog():
    event_handler = SourceChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./client', recursive=True)
    print("Starting watchdog")
    observer.start()
    while True:
        time.sleep(1)
