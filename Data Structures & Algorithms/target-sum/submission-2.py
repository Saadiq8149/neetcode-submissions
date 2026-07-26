from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, curr):
            if i == len(nums):
                return curr == target
            
            add = dfs(i+1, curr+nums[i])
            sub = dfs(i+1, curr-nums[i])
            return add + sub

        return dfs(0, 0)