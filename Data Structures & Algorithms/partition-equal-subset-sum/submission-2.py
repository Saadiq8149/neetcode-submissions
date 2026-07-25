class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)

        if arr_sum % 2 != 0:
            return False

        def dp(nums, s=0, index=0):
            if index >= len(nums):
                return False

            if s == arr_sum / 2:
                return True

            for i in range(index+1, len(nums)):
                if dp(nums, s+nums[i], i):
                    return True

            return False

        return dp(nums)