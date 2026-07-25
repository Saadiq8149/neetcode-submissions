class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [{'p': position[i], 's':speed[i]} for i in range(len(position))]
        cars = sorted(cars, key=lambda x:x['p'], reverse=True)
        
        fleets = []

        for i in range(len(cars)):
            time = (target - cars[i]['p'])/cars[i]['s']
            
            if not fleets or time > fleets[-1]:
                fleets.append(time)
    
        return len(fleets)