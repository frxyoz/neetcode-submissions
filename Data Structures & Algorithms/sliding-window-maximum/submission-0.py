class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = [0] * (len(nums) + 1 - k)
        l, r = 0, k-1
        while r < len(nums):
            arr[l] = max(nums[l:r+1])
            l+=1
            r+=1
        return arr