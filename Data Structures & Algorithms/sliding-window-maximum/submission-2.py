class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = k

        n = len(nums)
        while r <= n:
            m = nums[l]
            for i in range(l, r):
                m = max(m, nums[i])

            res.append(m)
            r += 1
            l += 1

        return res