class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         alice=0
#         bob=0
#         while len(piles) != 0:
#             if piles[0]>=piles[-1]:
#                 alice += piles[0]
#                 piles.pop(0)
            
#             else:
#                 alice += piles[-1]
#                 piles.pop(-1)
            
#             if piles[0]>=piles[-1]:
#                 bob += piles[-1]
#                 piles.pop(-1)
            
#             else:
#                 bob += piles[0]
#                 piles.pop(0)
        
#         print(alice, bob)

#         return True if alice >= bob else False
