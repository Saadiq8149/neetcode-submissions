class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        
        l = 0
        r = len(piles) - 1

        while l<r:
            if piles[l] >= piles[r]:
                alice += piles[l]
                l += 1
            else:
                alice += piles[r]
                r -= 1
            if piles[l] >= piles[r]:
                bob += piles[l]
                l += 1
            else:
                bob += piles[r]
                r -= 1        
        if alice >= bob:
            return True
        else:
            return False


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice=0
        bob=0
        while len(piles) != 0:
            if piles[0]>=piles[-1]:
                alice += piles[0]
                piles.pop(0)
            
            else:
                alice += piles[-1]
                piles.pop(-1)
            
            if piles[0]>=piles[-1]:
                bob += piles[-1]
                piles.pop(-1)
            
            else:
                bob += piles[0]
                piles.pop(0)
        
        print(alice, bob)

        return True if alice >= bob else False
