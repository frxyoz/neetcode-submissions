class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0, 1
        longest = 1
        while r < len(s):
            print(str(l) + "" + str(r))
            print(s[r])
            print(s[l:r])
            if s[r] in s[l:r]:
                l += 1
                if r == l:
                    r += 1
            else:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                r += 1
        return longest