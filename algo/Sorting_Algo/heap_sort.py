def build_max_heap():
    # array are global variables
    n = len(array)
    for i in range(n // 2, -1, -1):
        max_heapify(i)


def max_heapify(i):
    L = i * 2 + 1
    r = i * 2 + 2
    if L <= heapSize and array[L] > array[i]:
        large = L
    else:
        large = i
    if r <= heapSize and array[r] > array[large]:
        large = r
    if large != i:
        array[i], array[large] = array[large], array[i]
        max_heapify(large)


def heap_sort():
    global heapSize
    build_max_heap()
    for i in range(len(array) - 1, -1, -1):
        # exchange arr[0] with arr[i]
        array[0], array[i] = array[i], array[0]
        heapSize -= 1
        max_heapify(0)
global heapSize
array = [15, 3, 17, 18, 20, 2, 1, 666]
heapSize = len(array) - 1
heap_sort()
print(array)
