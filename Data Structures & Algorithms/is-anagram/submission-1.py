class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        chars = { l:0 for l in s }

        for l in s:
            chars[l] += 1

        for l in t:
            if not l in chars:
                return False
            chars[l] -= 1

        for k in chars:
            if chars[k] > 0:
                return False
        
        return True