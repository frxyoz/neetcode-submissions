class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def bt(arr, acc):
            # Base case: if no elements are left, we found a valid permutation
            if not arr:
                res.append(acc)
                return
            
            # Explore all possible choices for the next number
            for i in range(len(arr)):
                bt(arr[:i] + arr[i+1:], acc + [arr[i]])
                
        bt(nums, [])
        return res
