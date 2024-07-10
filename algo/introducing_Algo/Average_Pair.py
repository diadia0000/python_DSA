def averagePair(arr, avg):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) / 2 == avg:
                print(f"{arr[i]} and {arr[j]} are the Pair")


def averagePair_pointer(arr, avg):
    left = 0
    right = len(arr) - 1
    while right > left:
        mid = (arr[left] + arr[right]) / 2
        if mid > avg:
            right -= 1
        elif mid < avg:
            left += 1
        elif mid == avg:
            print(f"{arr[left]} and {arr[right]} are the Pair")
            left += 1
            right -= 1


averagePair([-11, 0, 1, 2, 3, 9, 14, 17, 21], 1.5)
print("\n")
averagePair_pointer([-11, 0, 1, 2, 3, 9, 14, 17, 21],1.5)
