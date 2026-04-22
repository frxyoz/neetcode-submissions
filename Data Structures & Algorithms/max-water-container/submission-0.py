class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        l, r = 0, len(heights)-1
        while r > l:
            width = r - l
            height = width * min(heights[l], heights[r])
            max_height = max(max_height, height)
            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        return max_height

        