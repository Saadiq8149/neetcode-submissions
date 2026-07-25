class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        res = 0

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
