from random import randint
from timeit import *

# common bubble sort
def bubbleSort_ASC(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# improved bubble sort
def bubbleSort2_ASC(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        change = False
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change = True
        if change == False:
            break
    return arr

for i in range(5):
    lst = [randint(1, 5001) for i in range(500)]
    t1 = Timer("bubbleSort_ASC(lst)", "from __main__ import bubbleSort_ASC, lst")
    t2 = Timer("bubbleSort2_ASC(lst)", "from __main__ import bubbleSort2_ASC, lst")
    t1_performance = t1.timeit(number = 20)
    t2_performance = t2.timeit(number = 20)
    print("  common bubble sort * 20 times :", '%.5f' % t1_performance, "seconds")
    print("improved bubble sort * 20 times :", '%.5f' % t2_performance, "seconds")
    print("The two Algorithms differ by", "%d" % (t1_performance/t2_performance), "times in performance.\n")