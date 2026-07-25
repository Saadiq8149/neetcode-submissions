class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  
        combinations = []
        
        def helper(start, current, currentSum):
            if currentSum == target:
                combinations.append(current.copy())
                return
            if currentSum > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                helper(i + 1, current, currentSum + nums[i]) 
                current.pop()

        helper(0, [], 0)
        return combinations
