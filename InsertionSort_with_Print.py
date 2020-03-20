# Insertion Sort

def insertionSort_ASC(arr):
    n = len(arr)
    for i in range(1, n):
        print('\n{}번째 loop 시작\n'.format(i))
        print('S =', arr[:i], 'U =', arr[i:], '\t# {}번째 loop에서 정렬 전'.format(i))
        val = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            print('S =', arr[:i], 'U =', arr[i:])
            pos -= 1
        if pos == i:
            pass
        else:
            arr[pos] = val
            print('S =', arr[:i], 'U =', arr[i:])
        print('S =', arr[:i+1], 'U =', arr[i+1:], '\t# {}번째 loop에서 정렬 후'.format(i))
    print('\n정렬 종료')

from random import randint
lst = [randint(1, 51) for i in range(7)]
insertionSort_ASC(lst)