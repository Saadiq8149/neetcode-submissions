class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        print(nums)

        if len(nums) == 0:
            return 0

        consecutive = 1
        maxConsecutive = 1
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                consecutive+=1
            elif nums[i+1]-nums[i] >= 1:
                consecutive = 1 
            maxConsecutive = max(consecutive, maxConsecutive)

        return maxConsecutive