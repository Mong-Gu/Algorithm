# def partition(arr, start, end):
#     pivot = arr[start]
#     L = start
#     R = end
#     done = False

#     while not done:
#         while L <= R and arr[L] <= pivot:
#             L += 1
#         while L <= R and pivot <= arr[R]:
#             R -= 1
#         if R < L:
#             done = True
#         else:
#             arr[L], arr[R] = arr[R], arr[L]
#     arr[start], arr[R] = arr[R], arr[start]
#     return R

# 퀵 정렬 (Quick Sort)

# 퀵 정렬 - 오름차순 (Quick Sort - Ascending)
def partition_ASC(arr, start, end):
    pivot = arr[start]
    L = start
    R = end
    done = False

    while not done:
        while L <= len(arr)-1 and arr[L] <= pivot:
            if L == len(arr)-1: # 리스트를 벗어나는 것을 방지
                break
            L += 1

        while R >= 0 and pivot < arr[R]:
            if R == 0: # 리스트를 벗어나는 것을 방지
                break
            R -= 1

        if R <= L: # 교차했다면
            done = True

        else: # 교차하지 않았다면
            arr[L], arr[R] = arr[R], arr[L]

    arr[start], arr[R] = arr[R], arr[start]
    return R

def quickSort_ASC(arr, start, end):
    if start < end:
        pivot = partition_ASC(arr, start, end)
        quickSort_ASC(arr, start, pivot - 1)
        quickSort_ASC(arr, pivot + 1, end)
    return arr
    
# 퀵 정렬 - 내림차순 (Quick Sort - Descending)
def partition_DESC(arr, start, end):
    pivot = arr[start]
    L = start
    R = end
    done = False

    while not done:
        while L <= len(arr)-1 and arr[L] >= pivot:
            if L == len(arr)-1: # 리스트를 벗어나는 것을 방지
                break
            L += 1

        while R >= 0 and pivot > arr[R]:
            if R == 0: # 리스트를 벗어나는 것을 방지
                break
            R -= 1

        if R <= L: # 교차했다면
            done = True

        else: # 교차하지 않았다면
            arr[L], arr[R] = arr[R], arr[L]

    arr[start], arr[R] = arr[R], arr[start]
    return R
    
def quickSort_DESC(arr, start, end):
    if start < end:
        pivot = partition_DESC(arr, start, end)
        quickSort_DESC(arr, start, pivot - 1)
        quickSort_DESC(arr, pivot + 1, end)
    return arr



from random import randint
lst = [randint(1, 101) for i in range(8)]
print('Quick Sort(ASC) :', lst, end=' '); quickSort_ASC(lst, 0, len(lst)-1); print('->', lst)

lst = [randint(1, 101) for i in range(8)]
print('Quick Sort(DESC) :', lst, end=' '); quickSort_DESC(lst, 0, len(lst)-1); print('->', lst)