class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif t == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif t == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                if (num1 < 0 and num2 > 0):
                    num1 *= -1
                    num1 = num1 // num2
                    stack.append(-1 * num1)
                elif (num1 > 0 and num2 < 0):
                    num2 *= -1
                    num1 = num1 // num2
                    stack.append(-1 * num1)
                else:
                    stack.append(num1 // num2)
            else:
                stack.append(int(t))
        return stack.pop()