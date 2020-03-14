import time
import multiprocessing as mp

def add_fast(n):
    count = 0
    for i in range(n):
        count += .001
    return count

def main():
    n_iter = 10
    pool = mp.Pool(mp.cpu_count())

    t0 = time.time()
    results = pool.map(add_fast,n_iter*[100000000])
    print("Summed to: ", sum(results))
    t1 = time.time()
    print("Time to run with multiprocesing: ", t1-t0)

    t0 = time.time()
    results = [add_fast(100000000) for i in range(n_iter)]
    print("Summed to: ", sum(results))
    t1 = time.time()
    print("Time to run without multiprocesing: ",t1-t0)

if __name__ == "__main__":
    main()
