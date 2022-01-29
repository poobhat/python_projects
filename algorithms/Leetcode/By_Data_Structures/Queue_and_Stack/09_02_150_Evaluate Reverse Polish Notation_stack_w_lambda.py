"""
Runtime: 72 ms, faster than 60.99%
Memory Usage: 14.3 MB, less than 96.51%
"""
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        operations = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b,
            "*": lambda a, b : a * b,
            "/": lambda a, b : int(a / b)
        }
        stack = []
        for tok in tokens:
            if tok in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                operation=operations[tok]
                stack.append(operation(num2, num1))
            else:
                stack.append(int(tok))
        return stack.pop()