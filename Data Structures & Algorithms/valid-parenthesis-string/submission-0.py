class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if len(left) != 0:
                    left.pop()
                elif len(star) != 0:
                    star.pop()
                else:
                    return False

        while left and star:
            l = left.pop()
            s = star.pop()
            if l >= s:
                return False

        return True if len(left) == 0 else False 
                