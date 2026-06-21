class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            elif not stack:
                return False
            else:
                t = stack.pop()
                if t == '[' and c != ']':
                    return False
                if t == '{' and c != '}':
                    return False
                if t == '(' and c != ')':
                    return False
        if stack:
            return False
        return True