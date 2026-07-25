class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        ans = []
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans
