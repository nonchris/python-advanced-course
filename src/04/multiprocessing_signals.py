import multiprocessing
import signal
import time
import sys

def child_process():
    print("Child process is running.")

    def child_signal_handler(sig, frame):
        print("Received SIGINT in child process. Exiting gracefully.")
        sys.exit(0)

    # Set up the signal handler for SIGINT (Ctrl+C) in the child process
    signal.signal(signal.SIGINT, child_signal_handler)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    print("Main process is running.")

    child_proc = multiprocessing.Process(target=child_process)
    child_proc.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Received Ctrl+C in main process. Terminating child process.")
        child_proc.terminate()
        child_proc.join()

    print("Main process finished.")
