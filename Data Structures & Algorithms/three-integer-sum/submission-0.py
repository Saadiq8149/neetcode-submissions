class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                if l < r and nums[l] + nums[r] < target:
                    l+=1
                elif l < r and nums[l] + nums[r] > target:
                    r-=1
                else:
                    ans.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans
