import multiprocessing
import time


def worker_function(a, b):
    result = a + b
    print(f"[{multiprocessing.current_process().name: <17}] {a+b = }")
    time.sleep(2)  # sleep to better visualize the result
    return result

if __name__ == "__main__":
    # List of argument tuples
    arguments = [(1, 2), (3, 4), (5, 6), (7, 8)] * 2

    # Create a pool of processes
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(worker_function, arguments)

    print("Results:", results)
