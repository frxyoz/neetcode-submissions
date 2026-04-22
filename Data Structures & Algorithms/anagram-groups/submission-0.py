class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            frequency = [0] * 26
            for x in string:
                frequency[ord(x) - 97] += 1
            frequency_tuple = tuple(frequency)
            if frequency_tuple in hashMap:
                hashMap[frequency_tuple].append(string)
            else: 
                hashMap[frequency_tuple] = [string]
        return list(hashMap.values())