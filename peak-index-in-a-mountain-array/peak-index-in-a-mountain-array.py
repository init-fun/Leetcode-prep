class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return -1
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            i = left + (right - left) // 2
            if arr[i-1] < arr[i] > arr[i+1]:
                return i
            else:
                # check which side we need to move
                if arr[i] < arr[i+1]:
                    left = i
                elif arr[i] > arr[i+1]:
                    right = i
            
            
        