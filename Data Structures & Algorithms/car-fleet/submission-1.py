class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((speed[i], position[i]))

        cars.sort(key=lambda x: x[1], reverse=True)

        stack = []
        for c in cars:
            time = (target - c[1]) / c[0]

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)

