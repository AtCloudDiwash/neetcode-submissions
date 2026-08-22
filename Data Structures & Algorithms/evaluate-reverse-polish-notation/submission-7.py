class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not token.lstrip("-").isdigit():
                if token == "+":
                    res = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "-":
                    res = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "*":
                    res = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                else:
                    res = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                    
            else:
                stack.append(int(token))
        return int(stack[-1])