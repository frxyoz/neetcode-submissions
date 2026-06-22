class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            if memo[i] == 1:
                return True
            if memo[i] == 0:
                return False
            for word in wordDict:
                lenWord = len(word)
                if i + lenWord <= len(s) and s[i:i+lenWord] == word:
                    if dfs(i + lenWord):
                        memo[i] = 1
                        return True
            memo[i] = 0
            return False
        
        return dfs(0)
            
