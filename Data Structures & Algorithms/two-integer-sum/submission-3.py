class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            if n in complement:
                index = complement[n]
                return [min(i, index), max(i, index)]

            complement[target - n] = i
            