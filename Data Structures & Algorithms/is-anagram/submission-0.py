class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        diction = dict()
        for char in s:
            if (char in diction.keys()):
                diction[char] += 1
            else:
                diction[char] = 1
        diction2 = dict()
        for char in t:
            if (char in diction2.keys()):
                diction2[char] += 1
            else:
                diction2[char] = 1
        return diction == diction2