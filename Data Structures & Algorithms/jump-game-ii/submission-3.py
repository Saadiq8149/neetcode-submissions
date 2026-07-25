class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums)-1:
            maxReach = 0
            for i in range(l, r+1):
                maxReach = max(maxReach, i+nums[i])

            l = r + 1
            r = maxReach
            res += 1

        return res
            