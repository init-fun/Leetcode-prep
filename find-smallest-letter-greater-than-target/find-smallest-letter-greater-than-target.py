class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) + 1 > 122:
            target = chr((ord(target) + 1) % 122 + 96)
        else:
            target = chr(ord(target) + 1)
        if target in letters:
            return target
        else:
            return self.nextGreatestLetter(letters, target)

            
            
        
        