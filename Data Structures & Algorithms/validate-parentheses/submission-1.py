class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
                continue
            
            if p == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
                continue
            
            if p == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
                continue

            stack.append(p)
        return len(stack) == 0