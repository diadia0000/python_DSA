import random
import time


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(arr1, arr2):
    result = []
    A, B = 0, 0
    while A < len(arr1) and B < len(arr2):
        if arr1[A] < arr2[B]:
            result.append(arr1[A])
            A += 1
        else:
            result.append(arr2[B])
            B += 1
    if A < len(arr1):
        result += arr1[A:]
    if B < len(arr2):
        result += arr2[B:]
    return result


my_array = [random.randint(-10000000, 1000000) for _ in range(500000)]
s = time.time()
my_array = merge_sort(my_array)
e = time.time()
print(e - s)
