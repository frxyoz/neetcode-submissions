class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        l1, r1 = intervals[0]

        for i in range(1, len(intervals)):
            l2, r2 = intervals[i]
            if r1 < l2:
                res.append([l1, r1])
                l1, r1 = l2, r2
            else:
                r1 = max(r1, r2)

        res.append([l1, r1])
        return res