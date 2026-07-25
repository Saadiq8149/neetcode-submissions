class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        res = r
        while l <= r:
            mid = (l + r) // 2

            curr = 0
            req = 1

            for w in weights:
                if curr + w > mid:
                    req += 1
                    curr = 0

                curr += w
            
            if req <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res