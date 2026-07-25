class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')

        l, r = 0, len(nums) - 1
        last = nums[-1]

        while l<=r:
            mid = (l + r) // 2
            
            if nums[mid] <= last:
                r = mid - 1
            else:
                l = mid + 1

        return nums[l]