class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        most = 0
        replacements = 0

        # print(Counter(s).most_common(1)[0][1])

        while r < len(s):
            if (r - l + 1) - Counter(s[l:r+1]).most_common(1)[0][1] > k:
                l += 1
            else:
                most = max(most, r-l+1)
                r += 1

        return most
        



