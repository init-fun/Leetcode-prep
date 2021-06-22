import collections
class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        max_counter = len(nums)//2 + 1
        d = collections.Counter(nums)
        for key, val in d.items():
            if val >= max_counter:
                return key