def mergeSort_ASC(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort_ASC(lefthalf)
        mergeSort_ASC(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
        # 이걸 빠져나오는 순간 lefthalf든 righthalf든 하나는 모든 원소를 다 쓴 것임
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf): # righthalf의 원소를 모두 썼을 경우
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf): # lefthalf의 원소를 모두 썼을 경우
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

def mergeSort_DESC(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort_DESC(lefthalf)
        mergeSort_DESC(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
        # 이걸 빠져나오는 순간 lefthalf, righthalf 둘 중 하나의 모든 원소는 다 쓴 것
            if lefthalf[i] > righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf): # righthalf의 원소를 모두 썼을 경우
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf): # lefthalf의 원소를 모두 썼을 경우
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

from random import randint
lst = [randint(1, 101) for i in range(8)]
print('Merge Sort(ASC) :', lst, end=' '); mergeSort_ASC(lst); print('->', lst)

lst = [randint(1, 101) for i in range(8)]
print('Merge Sort(DESC) :', lst, end=' '); mergeSort_DESC(lst); print('->', lst)

# 출처 : https://github.com/minsuk-heo/problemsolving/blob/master/sort/MergeSort.py (허민석님 코드)
