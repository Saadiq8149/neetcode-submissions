class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        l = 0
        while tickets[k] > 0:
            if tickets[l] > 0:
                tickets[l] -= 1
                time += 1
            l += 1
            if l == len(tickets):
                l = 0

        return time