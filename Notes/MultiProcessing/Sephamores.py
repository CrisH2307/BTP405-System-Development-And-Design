import multiprocessing

def worker(semaphore, data):
    with semaphore:
        # Access shared resource
        data.value += 1

if __name__ == "__main__":
    semaphore = multiprocessing.Semaphore(2)  # Allow two processes at a time
    shared_data = multiprocessing.Value("i", 0)
    
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker, args=(semaphore, shared_data))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Final value:", shared_data.value)
