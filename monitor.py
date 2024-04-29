import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import browser

class OnMyWatch:
    # Set the directory on watch
    watchDirectory = input("Enter Monitor Path: ")

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = None

    @staticmethod
    def debounce(wait):
        """ Decorator that will postpone a function's execution until after `wait` seconds
            have elapsed since the last time it was invoked. """
        def decorator(fn):
            def debounced(*args, **kwargs):
                def call_it():
                    fn(*args, **kwargs)
                if hasattr(debounced, 'timer'):
                    debounced.timer.cancel()
                debounced.timer = threading.Timer(wait, call_it)
                debounced.timer.start()
            return debounced
        return decorator

    @debounce(1.0)  # Debounce for 1 second
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Watchdog received modified event - {event.src_path}")
            browser.refresh()

if __name__ == '__main__':
    
    watch = OnMyWatch()
    watch.run()
