class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_ele = nums[0]
        profit = 0 
        for i in nums[1:]:
            min_ele = min(min_ele, i)
            profit = max(profit, i- min_ele)
        
        return profit 
    
        