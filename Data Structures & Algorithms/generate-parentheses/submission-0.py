class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets, current = [], ""

        def helper(n, brackets, current, left=0, right=0):
            if left == right and left == n:
                brackets.append(current)
                return

            if left < n:
                current += "("
                helper(n, brackets, current, left+1, right)
                current = current[:-1]
            if left > right and right < n:
                current += ")"
                helper(n, brackets, current, left, right+1)
            
        helper(n, brackets, current)
        return brackets