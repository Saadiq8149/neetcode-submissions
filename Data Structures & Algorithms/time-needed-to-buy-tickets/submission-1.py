class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time = 0

        # l = 0
        # while tickets[k] > 0:
        #     if tickets[l] > 0:
        #         tickets[l] -= 1
        #         time += 1
        #     l += 1
        #     if l == len(tickets):
        #         l = 0

        # return time

        time = 0

        for i in range(len(tickets)):
            if i < k:
                time += min(tickets[i], tickets[k])
            elif i > k:
                time += min(tickets[i], tickets[k] - 1)
            else:
                time += tickets[k]

        return time 
