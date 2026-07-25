class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        res = 0

        for j in range(n - 1, -1, -1):
            digit1 = ord(num1[j]) - ord("0")
            num = 0

            for i in range(m - 1, -1, -1):
                digit2 = ord(num2[i]) - ord("0")
                power = m - 1 - i

                num += digit1 * digit2 * (10 ** power)

            res += num * (10 ** (n - 1 - j))

        return str(res)