import threading
import time

lock = threading.Lock()

def get_lock_and_print():
    time.sleep(1)
    while True:
        if lock.acquire(blocking=True, timeout=1.0):
            print(f"[{threading.current_thread().name: <4}] Got the Lock!")
            lock.release()
            break
        print(f"[{threading.current_thread().name: <4}] Waiting...")

# Create thread that shall execute say_a_word(), with optional name
thread_1 = threading.Thread(target=get_lock_and_print, name="T1")

thread_1.start()  # Start the thread

with lock:
    print(f"[{'Main': <4}] Got the Lock!")
    time.sleep(5)
    print(f"[{'Main': <4}] Operation is over!")
