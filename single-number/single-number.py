class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # space = O(N)
        #time = O(N)
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i,v in d.items():
            if v < 2:
                return i
        