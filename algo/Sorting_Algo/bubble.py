import random
def bubble_sort(arr):
    global step,flag
    for i in range(len(arr)):
        flag = False
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                step+=1
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
        if not flag:
            break
    return arr
step = 0
test = [random.randint(0,10000) for i in range(10000)]
print(bubble_sort(test))
print(step)
