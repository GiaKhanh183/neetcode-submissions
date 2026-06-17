class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = int(0)
        for i in range(len(tokens)):
            if tokens[i] not in ["+","-","*","/"]:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                if tokens[i] == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                if tokens[i] == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                if tokens[i] == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
        return int((stack.pop()))