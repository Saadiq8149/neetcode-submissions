class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        real = sum(nums)
        theoretical = n*(n+1)/2

        return int(theoretical-real)