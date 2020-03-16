# Bubble Sort

def bubbleSort_ASC(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSort_DESC(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

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
                
lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', bubbleSort_ASC(lst))
lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', bubbleSort_DESC(lst))
lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', bubbleSort2_ASC(lst))