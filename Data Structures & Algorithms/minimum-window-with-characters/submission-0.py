class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs, counts = defaultdict(int), Counter(t)
        res = ""
        need = len(counts)
        have = 0

        l = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            if s[r] in counts and freqs[s[r]] == counts[s[r]]:
                have += 1
            while have == need:
                if res == "" or len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                freqs[s[l]] -= 1
                
                if s[l] in counts:
                    if freqs[s[l]] < counts[s[l]]:
                        have -= 1
                l += 1
                
        return res
            






            
        
