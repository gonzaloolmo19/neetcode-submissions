class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        corr = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                elif stack[-1] == corr[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0