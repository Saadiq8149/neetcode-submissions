class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n

        res = []
        for n in nums:
            if zeros and (zeros > 1 or n != 0):
                res.append(0)
            elif n == 0:
                res.append(product)
            else:
                res.append(product//n)

        return res