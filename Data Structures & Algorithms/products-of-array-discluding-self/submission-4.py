class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
            else:
                product *= num
        
        res = []
        for num in nums:
            if num == 0 and zero == 1:
                res.append(product)
            elif zero >= 1:
                res.append(0)
            else:
                res.append(product//num)
        return res
