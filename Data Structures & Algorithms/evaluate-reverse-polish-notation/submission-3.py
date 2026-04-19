class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(token)
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(b + a)
            elif token == "/" :
                tmp =  int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif token == "*":
                tmp = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif token == "-":
                tmp =  stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack[-1]