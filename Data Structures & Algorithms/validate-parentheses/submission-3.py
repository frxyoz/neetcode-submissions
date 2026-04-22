class Solution:
    def isValid(self, s: str) -> bool:
        gurt = []
        if not s:
            return False
        for char in s:
            if char == ')' and (len(gurt) == 0 or gurt.pop() != '('):
                return False
            if char == '}' and (len(gurt) == 0 or gurt.pop() != '{'):
                return False
            if char == ']' and (len(gurt) == 0 or gurt.pop() != '['):
                return False
            if char == '(' or char == '{' or char == '[':
                gurt.append(char)
        return len(gurt) == 0
            