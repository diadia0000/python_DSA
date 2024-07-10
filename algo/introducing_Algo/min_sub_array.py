class Solution:
    def minSubLength(self, array: list[int], k: int):
        right = 0
        left = 0
        minLength = float('Inf')
        cur = 0
        while right < len(array):
            cur += array[right]
            while cur >= k:
                if minLength > right - left + 1:
                    minLength = right - left + 1
                # update the value of minLength
                cur -= array[left]
                left += 1
            right += 1
        if (minLength == float('Inf')):
            return 0
        return minLength


print(Solution().minSubLength([0, 0, 0, 0, 0, 0, 1, 2], 11))
