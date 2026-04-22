class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictio = {}
        for gurt in nums:
            dictio[gurt] = dictio.get(gurt, 0) + 1
        print(dictio)
        freq = [[] for i in range(len(nums) + 1)] 
        for n, c in dictio.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)  
                if len(res) == k:
                    return res
        return