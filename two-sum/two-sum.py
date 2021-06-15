class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target
        # target - curr = y 
        # if y in list then return the num else not present
        tmp = {}
        for index, val in enumerate(nums):
            y = target - nums[index]
            if y in tmp:
                return [index, tmp[y]]
            else:
                tmp[val] = index 
                
                