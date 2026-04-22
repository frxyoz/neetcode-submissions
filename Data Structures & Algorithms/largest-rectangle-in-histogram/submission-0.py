class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i in range(len(heights)+1):
            left = i
            while stack and (i == len(heights) or stack[-1][1] > heights[i]):
                area = stack[-1][1] * (i - stack[-1][0])
                largest = max(largest, area)
                left = stack[-1][0]
                stack.pop()
            if i < len(heights):
                stack.append([left, heights[i]])
        return largest

        