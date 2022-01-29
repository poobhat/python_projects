"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any division
by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
"""
Runtime: 72 ms, faster than 60.99%
Memory Usage: 14.5 MB, less than 88.19%
"""
class Solution:
    def evaluate(self, num1, num2, operand):
        if operand == "+":
            return num2 + num1
        elif operand == "-":
            return num2 - num1
        elif operand == "*":
            return num2 * num1
        else:
            return int(num2/num1)

    def evalRPN(self, tokens: [str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        for tok in tokens:
            if tok in operands:
                first = stack.pop()
                second = stack.pop()
                stack.append(self.evaluate(first,second,tok))
            else:
                stack.append(int(tok))
        return stack.pop()


s = Solution()
tokens = ["4","13","5","/","+"]
print(s.evalRPN(tokens))