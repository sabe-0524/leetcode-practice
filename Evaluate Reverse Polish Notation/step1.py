from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                x = stack.pop()
                y = stack.pop()
                match token:
                    case "+":
                        stack.append(y + x)
                    case "-":
                        stack.append(y - x)
                    case "*":
                        stack.append(y * x)
                    case "/":
                        stack.append(int(y / x))
        
        return stack.pop()

