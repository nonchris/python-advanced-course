import multiprocessing

def printer():
    print(f"[{multiprocessing.current_process().name: <11}] Hello")

print(f"[{multiprocessing.current_process().name: <11}] {__name__}")


# TODO: take this line out
if __name__ == "__main__":

    process1 = multiprocessing.Process(target=printer)
    process2 = multiprocessing.Process(target=printer)

    process1.start()
    process2.start()


    process1.join()
    process2.join()
