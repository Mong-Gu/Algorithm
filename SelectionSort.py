# Selection Sort

def selectionSort_ASC(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selectionSort_DESC(arr):
    n = len(arr)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]       
    return arr     

lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', selectionSort_ASC(lst))
lst = [69, 10, 30, 2, 16, 8, 31, 22, 71, 27, 48, 6, 51, 50, 13, 98]; print(lst, end=''); print('->', selectionSort_DESC(lst))