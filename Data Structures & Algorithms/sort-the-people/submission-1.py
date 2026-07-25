class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       names = [(heights[i], names[i]) for i in range(len(names))]

       return [x[1] for x in sorted(names, reverse=True)] 