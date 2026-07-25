class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        
        seq = []

        for num in nums:
            if num-1 not in nums:
                seq.append(num)
        
        maxLen = 1
        for num in seq:
            next = num+1
            while next in nums:
                next+=1

            maxLen = max(maxLen, next-num)
        return maxLen