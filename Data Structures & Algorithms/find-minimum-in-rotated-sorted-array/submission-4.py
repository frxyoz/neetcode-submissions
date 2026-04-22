class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        value = nums[0]
        while nums[l] > nums[r]:
            m = l + (r - l) // 2
            value = nums[m]
            if value >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return min(nums[l], value)