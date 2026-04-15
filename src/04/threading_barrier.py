import threading
import time

#barrier = threading.Barrier(parties=2, action= lambda: print("All threads continued!"))

barrier = threading.Barrier(parties=3)

def wait_at_barrier():
    time.sleep(1)
    print(f"[{threading.current_thread().name: <4}] Reached barrier - waiting...")
    barrier.wait()
    print(f"[{threading.current_thread().name: <4}] Passed the barrier!")


threading.Thread(target=wait_at_barrier, name="T1").start()

threading.Thread(target=wait_at_barrier, name="T2").start()

print(f"[{'Main': <4}] Preparing something....!")
time.sleep(3)
print(f"[{'Main': <4}] Done.")
barrier.wait()
print(f"[{'Main': <4}] Passed the barrier!")
