class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2

        freq = Counter(nums)
        for n in freq:
            if freq[n] >= majority:
                return n


