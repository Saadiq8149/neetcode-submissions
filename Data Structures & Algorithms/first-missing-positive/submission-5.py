class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)        
        nums.sort()
  
        first_positive = None
        
        for i in range(len(nums)):
            if nums[i] > 0 and first_positive is None:
                first_positive = i
                if nums[first_positive] > 1:
                    return 1 

            if i == 0 or nums[i] <= 0 or nums[i-1] <= 0:
                continue

            if nums[i] - nums[i-1] > 1:
                return nums[i-1]+1 
        else:
            return nums[-1] + 1 if nums[-1] > 0 else 1    
