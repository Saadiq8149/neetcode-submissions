class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        duplicate = None

        while i < len(nums) - 1:
            if nums[i] == nums[i+1] and duplicate is None:
                duplicate = i + 1

            if nums[i] != nums[i+1] and duplicate is not None:
                nums[duplicate] = nums[i+1]
                duplicate += 1
            
            i += 1

        return len(nums) if duplicate is None else duplicate