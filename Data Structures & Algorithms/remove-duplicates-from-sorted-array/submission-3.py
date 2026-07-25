class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[write] = nums[r]
                write += 1

        return write