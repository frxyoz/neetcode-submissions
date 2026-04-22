class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suff = [0] * len(height)
        total_sum = 0
        lmax = 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            pref[i] = lmax
        rmax = 0
        for i in range(len(height)-1, 0, -1):
            rmax = max(rmax, height[i])
            suff[i] = rmax

        for i in range(1, len(height)-1):
            total_sum += min(pref[i], suff[i]) - height[i]
            print("added: " + str(min(pref[i], suff[i]) - height[i]))
        return total_sum


                
