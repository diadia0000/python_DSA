import random
import time
def quicksort(p, r):
    if p < r:
        q = partition(p, r)
        quicksort(p, q - 1)
        quicksort(q + 1, r)


def partition(p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


array = [random.randint(-10000, 1000) for _ in range(500000)]
s = time.time()
quicksort(0,500000-1)
print(array)
e = time.time()
print(e - s)
