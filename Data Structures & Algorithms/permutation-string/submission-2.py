class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)
        string1, string2 = [0] * 26, [0] * 26
        for char in range(len(s1)):
            string1[ord(s1[char])  - ord('a')] += 1
        for char in range(r):
            string2[ord(s2[char])  - ord('a')] += 1
        while r < len(s2):
            if string2 == string1:
                return True
            string2[ord(s2[l])  - ord('a')] -= 1
            string2[ord(s2[r])  - ord('a')] += 1
            l += 1
            r += 1

        return string2 == string1 