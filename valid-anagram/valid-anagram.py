from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = Counter(s)
        sec = Counter(t)
        if first == sec:
            return True
        
        return False