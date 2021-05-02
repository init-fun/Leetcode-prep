class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        charMap = {'}':'{',
                   ']':'[',
                   ')':'('
                   }
        
        for i in s:
            if i in charMap.values():
                stack.append(i)
            elif stack and charMap[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0