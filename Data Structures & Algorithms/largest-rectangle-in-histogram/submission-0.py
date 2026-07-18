from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (起始位置, 高度)
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            # 当前柱子更矮，说明栈里更高的柱子不能继续向右延伸
            while stack and stack[-1][1] > height:
                index, old_height = stack.pop()

                width = i - index
                max_area = max(max_area, old_height * width)

                # 当前柱子可以继承被弹出柱子的起点
                start = index

            stack.append((start, height))

        # 剩余柱子都可以一直延伸到数组末尾
        n = len(heights)

        for index, height in stack:
            width = n - index
            max_area = max(max_area, height * width)

        return max_area