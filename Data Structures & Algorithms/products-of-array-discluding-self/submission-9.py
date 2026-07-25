class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # zeros = 0
        # for n in nums:
        #     if n == 0:
        #         zeros += 1
        #     else:
        #         product *= n

        # res = []
        # for n in nums:
        #     if zeros and (zeros > 1 or n != 0):
        #         res.append(0)
        #     elif n == 0:
        #         res.append(product)
        #     else:
        #         res.append(product//n)

        # return res

        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        for i in range(n):
            if i > 0:
                prefixProduct[i] = prefixProduct[i-1]*nums[i-1] 

        for i in range(n-1, -1, -1):
            if i < len(nums)-1:
                suffixProduct[i] = suffixProduct[i+1]*nums[i+1]

        print(prefixProduct)
        print(suffixProduct)

        return [prefixProduct[i]*suffixProduct[i] for i in range(n)]