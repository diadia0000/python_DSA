from time import time
from random import randint


def selection_sort(arr):
    s = time()
    for i in range(0, len(arr) - 1):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    e = time()
    print(e - s)
    return arr


my_array = [1, 2, 3, 144, 5, 6, 7, 8, 9, 10]
my_array = selection_sort(my_array)
print(my_array)
