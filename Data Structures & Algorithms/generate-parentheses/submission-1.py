class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(i=0, left_open=0, curr=""):
            if i == 2*n:
                if not left_open:
                    res.append(curr)
                return

            if left_open:
                recurse(i+1, left_open-1, curr+")")
            recurse(i+1, left_open+1, curr+"(")

        recurse()
        return res