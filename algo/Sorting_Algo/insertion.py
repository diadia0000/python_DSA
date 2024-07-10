def insertion_sort(arr):
    for i in range(1, len(arr)):
        is_insert = arr[i]
        j = i-1
        while j>=0 and arr[j]>is_insert:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = is_insert
    return arr
my_array = [5,4,3,2,1]
my_array = insertion_sort(my_array)
print(my_array)