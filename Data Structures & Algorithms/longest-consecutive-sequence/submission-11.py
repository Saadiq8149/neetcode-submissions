class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()
        # curr = 1
        # longest = 1

        # n = len(nums)
        # for i in range(1, n):
        #     diff = nums[i] - nums[i-1]
        #     if diff == 1:
        #         curr += 1
        #         longest = max(curr, longest)
        #     elif diff == 0:
        #         continue
        #     else:
        #         curr = 1
        
        # return longest

        s = set(nums)

        longest = 0
        for n in nums:
            cons = 0
            if n-1 not in s:
                num = n
                while num in s:
                    num += 1
                    cons += 1
                longest = max(longest, cons)

        return longest