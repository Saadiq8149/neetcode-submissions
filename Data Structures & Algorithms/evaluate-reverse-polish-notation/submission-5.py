class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in "+*-/":
                right = s.pop()
                left = s.pop()
                if t == "+":
                    s.append(left + right)
                elif t == "*":
                    s.append(left * right)
                elif t == "-":
                    s.append(left - right)
                elif t == "/":
                    s.append(int(left / right))
            else:
                s.append(int(t))

        print(s)
        return s[0]
            