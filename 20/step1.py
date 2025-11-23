class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == "{":
                stack.append("{")
            elif c == "[":
                stack.append("[")
            elif c == ")":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "(":
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "{":
                    return False
            elif c == "]":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "[":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                