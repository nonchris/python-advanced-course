import multiprocessing
import time

# this is NOT how to use values
# GPT gave this as a prime example
def increment(counter: multiprocessing.Value):
    for _ in range(5):
        counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)  # "i" represents integer type, 0 is initial value

    process1 = multiprocessing.Process(target=increment, args=(counter,))
    process2 = multiprocessing.Process(target=increment, args=(counter,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Final counter value:", counter.value)
