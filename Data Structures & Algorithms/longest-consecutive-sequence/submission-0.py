class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for x in nums:
            if x not in numSet:
                numSet.add(x)
        print(numSet)
        longest = 0
        for x in numSet:
            cur = 1
            while x+1 in numSet:
                cur += 1
                x += 1
            longest = max(longest, cur)
        return longest