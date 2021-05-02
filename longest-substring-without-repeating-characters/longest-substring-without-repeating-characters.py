class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fptr = 0
        sptr = 0
        max_len = 0
        charSet = set()
        while sptr < len(s):
            if s[sptr] not in charSet:
                charSet.add(s[sptr])
                max_len = max(max_len, sptr - fptr + 1)
                sptr += 1
            else:
                charSet.remove(s[fptr])
                fptr+=1 
                
        return max_len
                
                
                
        