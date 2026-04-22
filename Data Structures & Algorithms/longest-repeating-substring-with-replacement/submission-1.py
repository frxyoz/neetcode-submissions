class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        maxReplacements = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxValue = 0
            for x in count.values():
                maxValue = max(x, maxValue)

            if (r - l + 1) - maxValue > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            maxReplacements = max(maxReplacements, r - l + 1)
            r += 1
        return maxReplacements
            


