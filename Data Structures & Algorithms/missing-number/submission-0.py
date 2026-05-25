class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for x in nums:
            n ^= x
        for x in range(len(nums)+1):
            n ^= x
        return n