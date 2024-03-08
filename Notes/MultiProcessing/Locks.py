import multiprocessing

def worker(lock, data):
    lock.acquire()
    try:
        # Access shared resource
        data.value += 1
    finally:
        lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    shared_data = multiprocessing.Value("i", 0)
    
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker, args=(lock, shared_data))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Final value:", shared_data.value)
