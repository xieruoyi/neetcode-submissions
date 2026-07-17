class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # 存还没找到更高温度的日期 index

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index

            stack.append(i)

        return result