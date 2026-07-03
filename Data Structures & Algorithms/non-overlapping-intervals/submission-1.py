class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                count += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end



        return count