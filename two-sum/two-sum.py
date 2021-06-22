class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,v in enumerate(nums):
            tmp_sum = target - v
            if tmp_sum not in d:
                d[v] = i
            else:
                return [i,d[tmp_sum]]
                
        