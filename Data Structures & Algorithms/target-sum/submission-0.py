class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(curr=0, pos=0):
            if curr == target and pos == len(nums):
                return 1

            if pos == len(nums):
                return 0

            return dp(curr-nums[pos], pos+1) + dp(curr+nums[pos], pos+1)

            
        return dp()