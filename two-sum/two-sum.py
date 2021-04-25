class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for index, val in enumerate(nums):
            # val + y = target
            # y = target - val
            y = target - val
            
            if y in tmp:
                second_index = tmp[y]
                return [index, second_index]
            else:
                tmp[val] = index