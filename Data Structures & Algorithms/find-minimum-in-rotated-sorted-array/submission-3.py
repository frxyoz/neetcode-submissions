class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        value = nums[0]
        while l < r:
            m = l + (r - l) // 2
            value = nums[m]
            if nums[l] < value and nums[r] < value:
                l = m + 1
            elif nums[l] < value:
                r = m - 1
            elif value == nums[l]:
                return min(value, nums[r])
            else:
                if nums[l] > nums[r]:
                    r = m
                else:
                    l = m
        return nums[l]