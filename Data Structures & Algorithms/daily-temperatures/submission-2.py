class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break

        return res
