import multiprocessing
import time

# we choose something mutable, so that *should* be able to work on the same reference
# hence the same object, spoiler: it won't work
variable: list[int | str] = [42, 32]


def process_fn():
    """ fn that will be executed inside a new process """
    print(f"[2nd] {variable=}, id={id(variable)}")
    time.sleep(5)
    print(f"[2nd] {variable=}, id={id(variable)}")
    variable.append("hello from 2")
    print(f"[2nd] {variable=}, id={id(variable)}")


if __name__ == "__main__":
    # Define the variable you want to print in the second process
    my_variable = "Hello, this is the variable!"

    # Create a new process
    process = multiprocessing.Process(target=process_fn)
    process.start()
    print(f"[main] {variable=}, id={id(variable)}")

    # wait and give process some time to start up
    time.sleep(2)

    variable.append(55)

    print(f"[main] {variable=}, id={id(variable)}")


    # Wait for the process to finish (optional)
    process.join()

    # The rest of the main process continues here
    print(f"[main] {variable=}, id={id(variable)}")
