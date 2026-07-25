class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffixMax = [-1] * len(arr)

        for i in range(len(arr)-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], arr[i+1])

        return suffixMax