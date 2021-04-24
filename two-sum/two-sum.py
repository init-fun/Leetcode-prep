class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fptr = 0
        while fptr < len(nums):
            sptr = fptr+1
            while sptr < len(nums):
                if nums[fptr] + nums[sptr] == target:
                    return [fptr, sptr]
                sptr += 1
            fptr += 1
        else:
            return False
            