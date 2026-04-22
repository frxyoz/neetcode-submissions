import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        for num in nums:
            dicti[num] = dicti.get(num, 0) + 1
        
        arr = [[] for _ in range(len(nums))]

        for key, value in dicti.items():
            arr[value-1].append(key)

        print(arr)
        j = 0
        ans = []
        for i in range(len(arr)-1, -1, -1):
            print(arr[i])
            for x in arr[i]:
                if j == k:
                    return ans
                ans.append(x)
                j += 1
        return ans
                

        
        
