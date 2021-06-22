class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def myfun(s):
            stack = []
            for i in s:
                if i!= '#':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
            return stack
        return myfun(s) == myfun(t)
        
        