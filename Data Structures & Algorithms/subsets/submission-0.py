class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currset = [], []

        def f(nums, l, s, c):
            if l >= len(nums):
                s.append(c.copy())
                return

            c.append(nums[l])
            f(nums, l+1, s, c)
            c.pop()
            f(nums, l+1, s, c)

        f(nums, 0, subsets, currset)

        return subsets



        