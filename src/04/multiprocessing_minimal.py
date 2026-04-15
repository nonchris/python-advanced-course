import multiprocessing
import time

def say_a_word(word: str):
    process_name = multiprocessing.current_process().name
    print(f"[{process_name: <17}] This is 'say_a_word()")
    time.sleep(1)
    print(f"[{process_name: <17}] '{word}' from '{process_name}'")


if __name__ == '__main__':

    # Create process
    process = multiprocessing.Process(target=say_a_word, args=("hello",), name=f"say_hello_process")
    process.daemon = True

    # Start the process
    process.start()

    # This print may appear in the same line as the first thread print
    print(f"[{multiprocessing.current_process().name: <17}] This is '__main__'")

    print(f"[{multiprocessing.current_process().name: <17}] This is '__main__' again")

    # Wait for threads to finish
    print(f"[{multiprocessing.current_process().name: <17}] Waiting for process...")
    # process.join()  # TODO: what happens when we comment this one out?

    print(f"[{multiprocessing.current_process().name: <17}] We're done")



