from threading import Lock, Thread
import time
counts = 0
def counter(by: int, lock: Lock):
    global counts
    with lock:
        print(f"Current value: {counts}, incrementing by {by}")
        time.sleep(0.1)  # Simulate some processing delay
        counts += by
        print(f"New value: {counts}")

if __name__ == "__main__":
    lock = Lock()
    threads = []
    for i in range(10, 50, 10):
        t = Thread(target=counter, args=(i, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    del threads[:]
    print("All threads started: {} {}".format(counts, threads))