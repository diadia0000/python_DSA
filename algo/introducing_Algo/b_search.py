from time import *
def b_search(arr,target):
    min = 0
    max = len(arr)-1
    while (min<=max):
        middle = (min+max)//2
        if target>arr[middle]: # too small
            min = middle+1
        elif target<arr[middle]: # to big
            max = middle-1
        elif target == arr[middle]:
            return target
    return -1

my_arr = [i for i in range(100000000)]
target = 1000001
s = time()
find = b_search(my_arr,target)
e = time()
print(e-s)
if find == target:
    print("yes")
else:
    print("no")
