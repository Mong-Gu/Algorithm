# Shell Sort

# 쉘 정렬 - 오름차순 (Shell Sort - Ascending)

def insertionSort_ASC(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] > val:
                arr[pos] = arr[pos-h]
                pos -= h
        arr[pos] = val
        i += h
        
def shellSort_ASC(arr):
    n = len(arr)
    h = n//2
    while h > 0:
        for i in range(0, h):
            insertionSort_ASC(arr, i, n-1, h)
        h //= 2
    return arr
    
    
    
# 쉘 정렬 - 내림차순 (Shell Sort - Descending)

def insertionSort_DESC(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] < val:
                arr[pos] = arr[pos-h]
                pos -= h
        arr[pos] = val
        i += h

def shellSort_DESC(arr):
    n = len(arr)
    h = n//2
    while h > 0:
        for i in range(0, h):
            insertionSort_DESC(arr, i, n-1, h)
        h //= 2
    return arr



from random import randint
lst = [randint(1, 101) for i in range(8)]
print('Shell Sort(ASC) :', lst, end=' '); print('->', shellSort_ASC(lst))

lst = [randint(1, 101) for i in range(8)]
print('Shell Sort(DESC) :', lst, end=' '); print('->', shellSort_DESC(lst))