import multiprocessing
import time

def producer(queue):
    messages_to_send = ["Message 1", "Message 2", "Message 3"]
    for msg in messages_to_send:
        queue.put(msg)
        time.sleep(1)  # Add a delay between messages
    queue.put(None)    # Signal the end of messages

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    producer_process.start()

    while True:
        message = queue.get()
        # None is explicitly used to signal the end of messages
        if message is None:
            break
        print("Received:", message)

    producer_process.join()
