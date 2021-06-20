class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        actual_sum = (n * (n-1))//2
        arr_sum = sum(nums)
        return abs(actual_sum - arr_sum)