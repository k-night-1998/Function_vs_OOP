class Solution:
    def binarySearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        result = -1  # store the index of first occurrence

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                result = mid
                # move left to find first occurrence
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:  # arr[mid] > k
                right = mid - 1

        return result