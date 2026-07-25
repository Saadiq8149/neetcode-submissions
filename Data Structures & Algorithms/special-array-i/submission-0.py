class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            a = nums[i]
            b = nums[i+1]

            if a % 2 == 0 and b % 2 == 0:
                return False
            if a % 2 == 1 and b % 2 == 1:
                return False
        return True