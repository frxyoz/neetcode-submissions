class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(ans)):
                if (i != j):
                    ans[j] *= nums[i]
        return ans