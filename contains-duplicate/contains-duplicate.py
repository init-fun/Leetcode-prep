class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = collections.Counter(nums)
        for i,val in x.items():
            if val > 1:
                return True