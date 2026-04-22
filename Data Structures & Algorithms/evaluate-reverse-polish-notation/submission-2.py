class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                float(s) # Tries to convert the string to a float
                return True
            except ValueError:
                # If a ValueError is caught, the string is not a valid number
                return False

        operands = []
        for char in tokens:
            if is_number(char):
                operands.append(int(char))
            else:
                if char == "+":
                    operands.append(int(operands.pop()) + int(operands.pop()))
                elif char == "-":
                    x = int(operands.pop())
                    y = int(operands.pop())
                    operands.append(y - x)
                elif char == "*":
                    operands.append(int(operands.pop()) * int(operands.pop()))
                else: 
                    x = int(operands.pop())
                    y = int(operands.pop())
                    operands.append(math.trunc(y / x))
            print(str(operands))
        return operands[0]


        