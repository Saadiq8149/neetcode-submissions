class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0

        if sum(gas) < sum(cost):
            return -1

        current = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                current = i+1
                tank = 0

        return current 