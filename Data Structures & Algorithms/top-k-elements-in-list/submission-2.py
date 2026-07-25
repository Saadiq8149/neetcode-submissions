class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        res = []
        count = 0

        for num in sorted(freq, key=freq.get, reverse=True):
            res.append(num)
            
            if count == k-1:
                return res
            count += 1

        return res