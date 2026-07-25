class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, current = [], []
        nums.sort()

        def helper(nums, current, subsets, i):
            if i == len(nums):
                subsets.append(current.copy())
                return


            current.append(nums[i])
            helper(nums, current, subsets, i+1)
            current.pop()
            
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            helper(nums, current, subsets, i+1)

        helper(nums, current, subsets, 0)
        return subsets
