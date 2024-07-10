def array_of_arrays(arr):
    if len(arr) == 0:
        return []
    for i in range(len(arr)):
        if type(arr[i]) != int:
            array_of_arrays(arr[i])
        else:
            print(arr[i],end = " ")

arr = [[0,[[[[1,2,]]],3,4,5]],6,[7],8,9,[[[[10]]]]]
array_of_arrays(arr)