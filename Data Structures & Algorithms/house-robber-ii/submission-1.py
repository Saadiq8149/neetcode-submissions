class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        res1 = 0

        dp = [0] * (len(nums) - 1)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        res1 = dp[-1]

        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            dp[i-1] = max(dp[i-2], nums[i]+dp[i-3])

        return max(res1, dp[-1])

