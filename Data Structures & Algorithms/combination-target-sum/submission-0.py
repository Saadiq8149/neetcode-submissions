class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        minValue = min(nums)

        combinations, current, currentSum, start = [], [], 0, 0

        def helper(nums, combinations, current, currentSum, start):
            if currentSum == target:
                combinations.append(current.copy())
            if currentSum + minValue > target:
                return

            for i in range(start, len(nums)):
                num = nums[i]
                current.append(num)
                currentSum += num
                helper(nums, combinations, current, currentSum, i)
                current.pop()
                currentSum -= num

        helper(nums, combinations, current, currentSum, start)
        return combinations