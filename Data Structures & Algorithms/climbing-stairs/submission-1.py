class Solution:
    def dp(self, n, cache):
        if n == 0 or n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = self.dp(n-1, cache) + self.dp(n-2, cache)
        return cache[n]

    def climbStairs(self, n: int) -> int:
        return self.dp(n, {})