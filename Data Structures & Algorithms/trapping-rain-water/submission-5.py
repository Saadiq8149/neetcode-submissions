class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        n = len(height)
        prefixMax = [0] * n
        suffixMax = [0] * n

        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], height[i+1])

        for i in range(n):
            w = min(prefixMax[i], suffixMax[i]) - height[i]

            if w > 0:
                water += w

        return water
