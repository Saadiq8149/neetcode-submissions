class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False

        if x < 0:
            isNeg = True

        rev = None

        if isNeg:
            rev = str(-1*x)[::-1]
            rev = int(rev)
        else:
            rev = str(x)[::-1]
            rev = int(rev)

        rev = -1*rev if isNeg else rev

        if rev > pow(2, 31)-1 or rev < -1*pow(2, 31):
            return 0

        return rev
