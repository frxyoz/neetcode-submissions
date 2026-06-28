class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []
        for triplet in triplets:
            for i in range(3):
                if triplet[i] > target[i]:
                    break
            else:
                good.append(triplet)
        
        one = two = three = False

        for triplet in good:
            if triplet[0] == target[0]:
                one = True
            if triplet[1] == target[1]:
                two = True
            if triplet[2] == target[2]:
                three = True
        
        return one and two and three
        