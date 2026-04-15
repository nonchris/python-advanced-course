import threading
import time

def say_a_word(word: str):
    thread_name = threading.current_thread().name
    print(f"[{thread_name: <16}] This is 'say_a_word()'")
    time.sleep(1)
    print(f"[{thread_name: <16}] '{word}' from '{thread_name}'")


if __name__ == '__main__':

    # Create thread
    thread = threading.Thread(target=say_a_word, args=("hello",), name=f"say_hello_thread")
    # thread.daemon = True  # TODO: what happens when we comment this in and .join() out?

    # Start the thread
    thread.start()

    # This print may appear in the same line as the first thread print
    print(f"[{threading.current_thread().name: <16}] This is '__main__'")

    print(f"[{threading.current_thread().name: <16}] This is '__main__' again")

    # Wait for threads to finish
    print(f"[{threading.current_thread().name: <16}] Waiting for thread...")
    # thread.join()  # TODO: what happens when we comment this one out?

    print(f"[{threading.current_thread().name: <16}] We're done")


# TODO: what happens if we define a daemon thread
#  that takes longer to execute than the current thread (as non daemon)?
#  will when will the program end?

