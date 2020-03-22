from random import randint
from timeit import *

# Insertion Sort
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = val
    return arr  


# Shell Sort
def insertionSort_forShellSort(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] > val:
                arr[pos] = arr[pos-h]
                pos -= h
        arr[pos] = val
        i += h
        
def shellSort(arr):
    n = len(arr)
    h = n//2
    while h > 0:
        for i in range(0, h):
            insertionSort_forShellSort(arr, i, n-1, h)
        h //= 2
    return arr

for i in range(5):
    lst = [randint(1, 10001) for i in range(10000)]
    # lst.sort(reverse = True) # 더욱 극단적인 상황으로 비교
    t1 = Timer("insertionSort(lst)", "from __main__ import insertionSort, lst")
    t2 = Timer("shellSort(lst)", "from __main__ import shellSort, lst")
    t1_performance = t1.timeit(number = 100)
    t2_performance = t2.timeit(number = 100)
    a = max(t1_performance, t2_performance)
    b = min(t1_performance, t2_performance)
    print("Insertion Sort * 100 times :", '%.5f' % t1_performance, "seconds")
    print("Shell Sort * 100 times :", '%.5f' % t2_performance, "seconds")
    print("The two Algorithms differ by", "%d" % (a/b), "times in performance.\n")
