# LC 20 Valid Parentheses

# WRONG
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{' ]:
                stack.append(c)
            else:
                top = stack.pop()
                if (c == ')' and top != '(') or \
                    (c == ']' and top != '[') or \
                    (c == '}' and top != '{'):
                    return False
        return not stack

