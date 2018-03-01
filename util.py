from multiprocessing import Manager, Process


def __parallel_process(method, urls):
    with Manager() as manager:
        L = manager.list()  # <-- can be shared between processes.
        processes = []
        for url in urls:
            p = Process(target=method, args=(L, url))  # Passing the list
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        result = [a for a in L]

    return result
