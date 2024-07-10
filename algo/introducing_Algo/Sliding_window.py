def maxSum(arr, n):
    if len(arr) < n:
        return -1
    max_sum = sum([arr[i] for i in range(n)])
    p1 = n
    p2 = 0
    ans = max_sum
    while p1 < len(arr):
        max_sum = max_sum - arr[p2] + arr[p1]
        ans = max(ans, max_sum)
        p2 += 1
        p1 += 1
    return ans


def minSum(arr, n):
    if len(arr) < n:
        return -1
    min_sum = sum([arr[i] for i in range(n)])
    p1 = n
    p2 = 0
    ans = min_sum
    while p1 < len(arr):
        min_sum = min_sum - arr[p2] + arr[p1]
        ans = min(ans, min_sum)
        p2 += 1
        p1 += 1
    return ans


Max = maxSum([2, 7, 3, 7, 25, 0, 6, 1, -5, -12, -11], 3)
Min = minSum([2, 7, 3, 0, 6, 1, -5, -12, -11], 3)
print(Max, Min)
