# Insertion Sort

def insertionSort_ASC(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = val
    return arr  

def insertionSort_DESC(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] < val:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = val
    return arr  

lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', insertionSort_ASC(lst))
lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', insertionSort_DESC(lst))
