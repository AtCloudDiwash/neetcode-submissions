class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for token in tokens:
            if not token.lstrip("-").isdigit():
                if token == '+':
                    res = int(stack[len(stack) - 2 ]) + int(stack[len(stack) - 1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == '-':
                    res = int(stack[len(stack) - 2 ]) - int(stack[len(stack) - 1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == '*':
                    res = int(stack[len(stack) - 2 ]) * int(stack[len(stack) - 1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                else:
                    res = int(int(stack[len(stack) - 2 ]) / int(stack[len(stack) - 1]))
                    stack.pop()
                    stack.pop()
                    stack.append(res)         
            else:
                stack.append(token)
        return int(stack[-1])
                
        