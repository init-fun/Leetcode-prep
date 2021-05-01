class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        max_len = 0
        lft_ptr = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[lft_ptr])
                lft_ptr += 1
            charSet.add(s[i])
            max_len = max(max_len, i-lft_ptr +1 )
        return max_len
        