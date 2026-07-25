class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in '+-*/':
                b = stack.pop()
                a = stack.pop()
                match c:
                    case '+':
                        stack.append(a + b)
                    case '-':
                        stack.append(a - b)
                    case '*':
                        stack.append(a * b)
                    case '/':
                        stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack[0]