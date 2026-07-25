class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        l = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while l <= r and s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
                print(l)

        return 0 if res == float('inf') else res
            
