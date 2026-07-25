class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        freq = {}
        for num in hand:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in hand:
            if freq[num] == 0:
                continue

            for n in range(num, num+groupSize):
                if n not in freq or freq[n] == 0:
                    return False
                else:
                    freq[n] -= 1

        return True
