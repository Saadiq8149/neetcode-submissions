class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(curr=0, pos=0):
            if (curr, pos) in memo:
                return memo[(curr, pos)]

            if curr == target and pos == len(nums):
                return 1

            if pos == len(nums):
                return 0

            memo[(curr, pos)] = dp(curr-nums[pos], pos+1) + dp(curr+nums[pos], pos+1)
            return memo[(curr, pos)]
            
        return dp()