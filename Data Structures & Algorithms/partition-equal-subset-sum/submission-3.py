class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)

        if arr_sum % 2 != 0:
            return False

        target = arr_sum // 2
        memo = {}

        def dp(nums, s=0, index=0):
            if s == target:
                return True

            if index >= len(nums) or s > target:
                return False

            if (index, s) in memo:
                return memo[(index, s)]

            for i in range(index, len(nums)):
                if dp(nums, s + nums[i], i + 1):
                    memo[(index, s)] = True
                    return True

            memo[(index, s)] = False
            return False

        return dp(nums)