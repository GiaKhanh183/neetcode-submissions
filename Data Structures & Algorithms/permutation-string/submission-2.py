class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            a = [i for i in s1]
            b = [j for j in s2]
        else:
            return False
        l = 0
        r = len(a) - 1
        while r < len(b):
            if sorted(a) == sorted(b[l:r+1]):
                return True
            l += 1
            r += 1
        return False