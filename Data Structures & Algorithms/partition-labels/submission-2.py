class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        i = 0
        start,end = 0, last[s[0]]
        res = []
        while i < len(s):
            end = max(end, last[s[i]])
            if i == end:
                res.append(end + 1 - start)
                start = i+1
            i += 1
        return res
