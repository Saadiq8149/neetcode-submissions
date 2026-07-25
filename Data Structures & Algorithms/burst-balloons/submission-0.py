class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}
        def dp(l=1, r=len(nums)-2):
            if (l, r) in memo:
                return memo[(l,r)]
            
            if l > r:
                return 0

            res = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dp(l, i-1) + dp(i+1, r)
                res = max(res, coins)

            memo[(l, r)] = res
            return res


        return dp()