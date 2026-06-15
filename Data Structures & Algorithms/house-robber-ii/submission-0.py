class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        first = [-1] * n
        last = [-1] * n

        def dfs1(i):
            if i >= n - 1:  # exclude last house
                return 0

            if first[i] != -1:
                return first[i]

            first[i] = max(
                nums[i] + dfs1(i + 2),
                dfs1(i + 1)
            )
            return first[i]

        def dfs2(i):
            if i >= n:
                return 0

            if last[i] != -1:
                return last[i]

            last[i] = max(
                nums[i] + dfs2(i + 2),
                dfs2(i + 1)
            )
            return last[i]

        return max(dfs1(0), dfs2(1))