class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def isPalindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                while left < right and not s[left].isalnum():
                    left += 1
                while left < right and not s[right].isalnum():
                    right -= 1
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
            return True


        def backtrack(j, i):
            if j == len(s):
                res.append(cur[:])
                return
            if isPalindrome(s[j:i+1]):
                cur.append(s[j:i+1])
                if i < len(s):
                    backtrack(i+1, i+1)
                cur.pop()
            if i < len(s):
                backtrack(j, i+1)
            

        backtrack(0,0)
        return res
