class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        n = len(digits)

        digits[-1] += 1

        carry = digits[-1] // 10
        digits[-1] = digits[-1] % 10

        for i in range(n-2, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
        
        if not carry:
            return digits
        else:
            return [carry] + digits
       