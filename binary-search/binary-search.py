class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            i = left + (right - left)//2
            if arr[i] == target:
                return i
            if arr[i] < target:
                left = i + 1
            else:
                right = i - 1
        return -1