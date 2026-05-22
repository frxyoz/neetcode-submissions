class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = set()

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    cur.append(num)
                    backtrack()
                    used.discard(num)
                    cur.pop()
            
        backtrack()
        return res

