class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            t = temperatures[i]
            while len(s) > 0 and s[-1][0] < t:
                result[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append((t, i))

        return result