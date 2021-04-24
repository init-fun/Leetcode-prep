class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        for i,j in d.items():
            if j < 2:
                return i
            