class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        fptr = 0
        sptr = len(arr) - 1
        res = [0] * len(arr)
        ptr = sptr
        while fptr <= sptr:
            left = arr[fptr] ** 2
            right = arr[sptr] ** 2
            if left <=right:
                res[ptr] = right
                sptr -= 1
                ptr -= 1
            else:
                res[ptr] = left
                fptr += 1
                ptr -= 1
        return res