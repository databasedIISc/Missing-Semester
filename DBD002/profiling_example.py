from line_profiler import profile as time_profile
from memory_profiler import profile as memory_profile
import time

@time_profile
def time_func():
    print("Time Profiling Example!")
    time.sleep(1)

    total = 0
    for i in range(1, 1001):
        total += i * i
    return total

@memory_profile
def memory_func():
    print("Memory Profiling Example!")

    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    time_func()
    memory_func()
