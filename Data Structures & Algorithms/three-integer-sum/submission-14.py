class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, num in enumerate(nums):
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(i) for i in res]