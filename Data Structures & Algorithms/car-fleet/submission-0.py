class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if they have the same number, the stack becomes only that set, and become the slower one
        
        cars = sorted(
            zip(position, speed),
            reverse=True
        )

        stack = []

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            stack.append(arrival_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)