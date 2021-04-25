class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])
        
        # O(n) till now
        res = [] # question said it will not be counted in the space compelexity
        for i,val in enumerate(nums):
            if val > 0:
                res.append(i+1)
        return res