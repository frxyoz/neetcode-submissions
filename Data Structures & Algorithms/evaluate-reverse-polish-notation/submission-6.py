class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for char in tokens:
            if char == "+":
                operands.append(int(operands.pop()) + int(operands.pop()))
            elif char == "-":
                x = int(operands.pop())
                y = int(operands.pop())
                operands.append(y - x)
            elif char == "*":
                operands.append(int(operands.pop()) * int(operands.pop()))
            elif char == "/":
                a, b = operands.pop(), operands.pop()
                operands.append(int(float(b) / a))
            else: 
                operands.append(int(char))
        return operands[0]


        