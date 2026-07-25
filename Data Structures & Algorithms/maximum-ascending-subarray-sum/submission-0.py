class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = nums[0]

        prev = nums[0]
        for n in nums[1:]:
            if n <= prev:
                sum = n
                prev = n
            else:
                sum += n
                prev = n
            maxSum = max(sum, maxSum)

        return maxSum
