class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        res = 0
        for i in range(len(nums)):
            curr = 1
            currNum = nums[i]
            if currNum-1 not in hashset:
                while currNum+1 in hashset:
                    currNum += 1
                    curr += 1
            res = max(res, curr)

        return res
