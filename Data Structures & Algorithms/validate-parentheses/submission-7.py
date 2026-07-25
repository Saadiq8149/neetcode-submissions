class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        for c in s:
            if c in "({[":
                o.append(c)
            if c == "}":
                if not o or o[-1] != "{":
                    return False
                else:
                    o.pop()
            elif c == "]": 
                if not o or o[-1] != "[":
                    return False
                else:
                    o.pop()
            elif c == ")":
                if not o or o[-1] != "(":
                    return False
                else:
                    o.pop()

        return False if len(o) > 0 else True 