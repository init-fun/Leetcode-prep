class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        new_min = arr[0]
        old_max = 0
        for i in range(1, len(arr)):
            if arr[i] <= new_min:
                new_min = arr[i]
            old_max = max(old_max, arr[i] - new_min)
        return old_max