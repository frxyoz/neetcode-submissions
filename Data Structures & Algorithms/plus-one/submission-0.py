class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == []:
            return [1]
        elif digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1
        else:
            digits = self.plusOne(digits[:len(digits)-1]) + [0]
        return digits
