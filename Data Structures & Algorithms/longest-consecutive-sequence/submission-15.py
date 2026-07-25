class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)

        res = 1
        curr = 1
        for i in range(len(nums)):
            currNum = nums[i]
            if currNum-1 not in hashset:
                while currNum+1 in hashset:
                    currNum += 1
                    curr += 1
            res = max(res, curr)
            curr = 1


        return res
