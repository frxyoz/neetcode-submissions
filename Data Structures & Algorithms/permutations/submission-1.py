class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack()
                    cur.pop()
            
        backtrack()
        return res

