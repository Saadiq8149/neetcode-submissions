class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffixMax = [0] * len(arr)

        for i in range(len(arr) - 2, -1, -1):
            suffixMax[i] = max(arr[i+1], suffixMax[i+1])

        print(suffixMax)

        for i in range(len(arr)-1):
            arr[i] = suffixMax[i]

        arr[-1] = -1

        return arr