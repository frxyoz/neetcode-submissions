class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            for j in range(i, len(candidates)):
                # skip duplicates at the same recursion depth
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # optional pruning since array is sorted
                if total + candidates[j] > target:
                    break

                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

        dfs(0, [], 0)
        return res