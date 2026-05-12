class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, runningSum):
            if i >= len(nums) or runningSum > target:
                return
            elif runningSum == target:
                if cur not in res:
                    res.append(cur.copy())
            else:
                cur.append(nums[i])
                dfs(i, runningSum + nums[i])
                cur.pop()
                dfs(i+1, runningSum)
        
        dfs(0, 0)
        return res



                
