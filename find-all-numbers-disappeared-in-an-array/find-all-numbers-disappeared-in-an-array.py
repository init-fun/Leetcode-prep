class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_len = len(nums) # O(n) 
        
        tmp = {} # O(n) space
        
        for i in nums:
            if i in tmp:
                pass
            else:
                tmp[i] = 1
                
        res = [] # extra space 
        
        for i in range(1,max_len+1):
            if i not in tmp:
                res.append(i)
        
        return res
        