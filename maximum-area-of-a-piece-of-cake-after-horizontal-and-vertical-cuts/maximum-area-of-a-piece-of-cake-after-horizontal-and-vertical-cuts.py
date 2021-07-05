class Solution:
    
    
    
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        def getMax(cuts):
            max_diff = cuts[0]
            for i in range(1, len(cuts)):
                max_diff = max(abs(cuts[i] - cuts[i -1]), max_diff)
            return max_diff
        hc.sort()
        vc.sort()
        hc+=[h]
        vc += [w]
        return (getMax(hc) * getMax(vc)) % (pow(10, 9) + 7)