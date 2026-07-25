class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

        print(prefixProduct)
        print(suffixProduct)


        res = []
        for i in range(n):
            curr = 1
            if i > 0:
                curr *= prefixProduct[i]
            if i < n-1:
                curr *= suffixProduct[i]
            res.append(curr)

        return res
