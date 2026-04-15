import multiprocessing
import os
import signal
import time


def infinite_loop():
    while True:
        print("I'm unstoppable! - Wheeee!")

# Start child
child = multiprocessing.Process(target=infinite_loop)
child.start()

# Wait for a few seconds
time.sleep(3)

# Kill the child using SIGKILL
print("That's enough...")
os.kill(child.pid, signal.SIGKILL)
print(f"No you're not. ~parent")
