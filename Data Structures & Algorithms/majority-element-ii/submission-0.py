class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        majority = len(nums) // 3

        res = []
        for n in freq:
            if freq[n] > majority:
                res.append(n)

        return res