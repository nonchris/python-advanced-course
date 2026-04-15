import multiprocessing
from multiprocessing.connection import Connection
import time

def sender(pipe: Connection):
    messages_to_send = ["Message 1", "Message 2", "Message 3"]
    for msg in messages_to_send:
        pipe.send(msg)
        time.sleep(0.5)  # Add a delay between messages

    pipe.close()

if __name__ == "__main__":
    parent_side, child_side = multiprocessing.Pipe()

    sender_process = multiprocessing.Process(target=sender, args=(parent_side,))
    sender_process.start()

    while True:
        # try to get a new message, timeout after two seconds
        if child_side.poll(timeout=2):
            # read data
            received_data = child_side.recv()
            print("Received:", received_data)
        else:
            print("No more messages.")
            break

    sender_process.join()
    child_side.close()

