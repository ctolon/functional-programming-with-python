"""Multiprocessing example with fp"""
import collections
from pprint import pprint
import time
import multiprocessing
import os
import concurrent.futures

Scientist = collections.namedtuple("Scientist", [
    "name",
    "field",
    "born_in",
    "nobel"
])

scientists = (
    Scientist(name="Ada Lovelace", field="math", born_in=1815, nobel=False),
    Scientist(name="Albert Einstein", field="physics", born_in=1879, nobel=True),
    Scientist(name="Emmy Noether", field="math", born_in=1882, nobel=False),
    Scientist(name="Marie Curie", field="chemistry", born_in=1867, nobel=True),
    Scientist(name="Tu Youyou", field="chemistry", born_in=830, nobel=False),
    Scientist(name="Ada Yonath", field="astronomy", born_in=1815, nobel=False),
    Scientist(name="Vera Rubin", field="astronomy", born_in=1815, nobel=False),
    Scientist(name="Sally Ride", field="physics", born_in=1815, nobel=False)
)

pprint(scientists)
print()

def transform(x: Scientist):
    print(f"Processing {os.getpid()} working record {x.name}")
    time.sleep(1)
    result = {'name': x.name, 'age': 2017 - x.born_in}
    print(f"Process {os.getpid()} Done processing record {x.name}")
    return result


# For Classical Run Benchmark
print("Classical One Thread One Process Run...")
start_classic = time.time()
result = tuple(map(transform, scientists))
end_classic = time.time()
print(f"Time to complete: {end_classic - start_classic:.2f}s\n")
# pprint(result)

# For Multiprocessing Run Benchmark
print("Multiprocessing Run (Multi Process One Thread)...")
start_multiprocessing = time.time()
with multiprocessing.Pool() as pool:
    result = pool.map(transform, scientists)
end_multiprocessing = time.time()
print(f"Time to complete: {end_multiprocessing - start_multiprocessing:.2f}s\n")
# pprint(result)

# For Concurrent Futures Process Executor Run Benchmark
print("Concurrent Futures Process Executor Run.. (Multi Process One Thread)")
start_process_executor = time.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    result = executor.map(transform, scientists)
end_process_executor = time.time()
print(f"Time to complete: {end_process_executor - start_process_executor:.2f}s\n")
# pprint(result)
    

# For Concurrent Futures Thread Executor Run Benchmark
print("Concurrent Futures Thread Executor Run.. (One Process Multithread)")
start_thread_executor = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.map(transform, scientists)
end_thread_executor = time.time()
print(f"Time to complete: {end_thread_executor - start_thread_executor:.2f}s\n")
# pprint(result)