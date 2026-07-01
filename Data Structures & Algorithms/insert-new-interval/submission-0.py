class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        l, r = newInterval[0], newInterval[-1]
        merged = False
        for i in range(len(intervals)):
            x, y = intervals[i][0], intervals[i][1]
            if y < l:
                output.append([x, y])
            elif x > r:
                if not merged:
                    output.append([l, r])
                    merged = True
                output.append([x, y])
            else:
                l = min(l, x)
                r = max(r, y)
        if not merged:
            output.append([l, r])
        return output
            