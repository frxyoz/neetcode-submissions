class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)
        s = sorted(s1)
        while r <= len(s2):
            if sorted(s2[l:r]) == s:
                return True
            l += 1
            r += 1
        return False