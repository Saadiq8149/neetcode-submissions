class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for v in freq.values():
            if v % 2 != 0:
                return False

        return True