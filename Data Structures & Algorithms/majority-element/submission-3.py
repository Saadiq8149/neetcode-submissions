class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority = len(nums) // 2

        # freq = Counter(nums)
        # for n in freq:
        #     if freq[n] >= majority:
        #         return n

        candidate = nums[0]
        votes = 1
        for n in nums[1:]:
            if n == candidate:
                votes += 1
            else:
                votes -= 1

            if votes == 0:
                candidate = n
                votes = 1

        return candidate


