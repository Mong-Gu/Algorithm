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
        print('\n------------- 간격(interval) =', h, '------------------')
        for i in range(0, h):
            print('\n정렬 전 :', arr)
            print('부분 집합에 포함된 원소 :', [elem for idx, elem in enumerate(arr) if idx % h == i])
            # h = 4 , [0, 1, 2, 3, 4, 5, 6, 7]
            insertionSort_ASC(arr, i, n-1, h)
            print('정렬 후 :', arr)
        h //= 2
    print('\n정렬 종료')

from random import randint
# lst = [1,2,3,4,5,6,7,8]
lst = [randint(1, 101) for i in range(8)]
shellSort_ASC(lst)