from threading import Lock, Thread
import time

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def increment(self, by):
        with self._lock:
            print(f"Current value: {self.value}, incrementing by {by}")
            time.sleep(0.1)  # Simulate some processing delay
            self.value += by
            print(f"New value: {self.value}")


if __name__ == "__main__":
    counter = Counter()
    threads = []
    for i in range(10, 50, 10):
        t = Thread(target=counter.increment, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {counter.value}")