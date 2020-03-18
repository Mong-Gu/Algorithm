# 버블 정렬 (Bubble Sort)

# 버블 정렬 - 오름차순 (Bubble Sort - Ascending)
def bubbleSort_ASC(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 버블 정렬 - 내림차순 (Bubble Sort - Descending)
def bubbleSort_DESC(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# 개선된 버블 정렬 - 오름차순 (Improved Bubble Sort - Ascending)
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

# 난수를 생성하여 test해보기 (Test by random number) 
from random import randint

lst = [randint(1, 100) for i in range(5)]
print('Bubble Sort(ASC) :', lst, end=' '); print('->', bubbleSort_ASC(lst))
lst = [randint(1, 100) for i in range(5)]
print('Bubble Sort(DESC) :', lst, end=' ');print('->', bubbleSort_DESC(lst))
lst = [randint(1, 100) for i in range(5)]
print('Improved Bubble Sort(ASC) :', lst, end=' ');print('->', bubbleSort2_ASC(lst))