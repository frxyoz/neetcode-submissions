class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def build(arr, i):
            nonlocal ans
            if i == len(nums):
                ans.add(tuple(arr))
                return
            else:
                build(arr + [nums[i]], i+1)
                build(arr, i+1)

        build([], 0)
        return [list(x) for x in ans]