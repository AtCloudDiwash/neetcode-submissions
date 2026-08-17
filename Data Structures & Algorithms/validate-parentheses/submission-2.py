class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                elif stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False


            

