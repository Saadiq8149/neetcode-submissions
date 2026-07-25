class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            s = numbers[L] + numbers[R]
            if s < target:
                L+=1
            elif s > target:
                R-=1
            else:
                return [L+1, R+1]