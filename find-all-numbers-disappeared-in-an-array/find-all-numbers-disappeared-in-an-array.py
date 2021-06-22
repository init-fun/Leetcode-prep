from collections import Counter
class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        # time limit exceeded
        
        # res = []
        # for i in range(1,len(nums)+1):
        #     if i in nums:
        #         continue
        #     res.append(i)
        # return res
        res = []
        arr_len = len(arr)
        for i in range(arr_len):
            index = abs(arr[i]) - 1
            arr[index] = -1 * abs(arr[index])
        
        for i in range(arr_len):
            if arr[i] > 0:
                res.append(i+1)
        return res
        
        