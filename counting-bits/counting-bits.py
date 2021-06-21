class Solution:
    
    def countBits(self, n: int) -> List[int]:
        res = []
        def myfun(x):
            count = 0
            while x != 0:
                x, y = divmod(x, 2)
                if y == 1:
                    count += 1
            return count
        
        
        for i in range(n+1):
            # x = 
            res.append(myfun(i))
        return res