class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = 0
        rmax = 0
        l, r = 0, len(height)-1
        sum = 0
        while (l <= r):
            if lmax < rmax:
                lmax = max(lmax, height[l])
                sum += lmax - height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                sum += rmax - height[r]
                r-=1
        return sum





                
