class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(nlogn)
        target = 0
        
        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                new_sum = val+ nums[left]+nums[right]
                if new_sum > target:
                    right -= 1
                elif new_sum < target:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left +=1 
                    
                    while left < right and nums[left] == nums[left -1]:
                        left +=1
        return res