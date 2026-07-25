class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = Counter(nums)

        i = 0
        for k in freq:
            nums[i] = k
            i += 1

        return i