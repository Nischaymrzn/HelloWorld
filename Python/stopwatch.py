import time
def stopwatch():
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print(f"Elapsed time: {end - start} seconds")
