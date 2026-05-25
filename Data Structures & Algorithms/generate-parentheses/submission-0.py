class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, opens, closes):
            if opens == n and closes == n:
                res.append("".join(curr))
                return
            if closes > opens:
                return
            if opens < n:
                curr.append("(")
                backtrack(curr, opens + 1, closes)
                curr.pop()
            if closes < n:
                curr.append(")")
                backtrack(curr, opens, closes+1)
                curr.pop()
        
        backtrack([], 0, 0)

        return res
            
