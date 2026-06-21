class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSeen = 0
        minArr, maxArr = [0] * len(nums), [0] * len(nums)
        maxSeen = minArr[0] = maxArr[0] = nums[0]

        for i in range(1, len(nums)):
            minArr[i] = min(nums[i], nums[i] * minArr[i-1], nums[i] * maxArr[i-1])
            maxArr[i] = max(nums[i], nums[i] * maxArr[i-1], nums[i] * minArr[i-1])
            maxSeen = max(maxArr[i], maxSeen)


        return maxSeen