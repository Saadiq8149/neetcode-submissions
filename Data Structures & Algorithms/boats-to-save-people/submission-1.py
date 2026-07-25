class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = len(people)

        people.sort()
        l, r = 0, len(people) - 1

        while l < r:
            if people[r] + people[l] <= limit:
                l += 1
                r -= 1
                boats -= 1
            else:
                r -= 1
        

        return boats