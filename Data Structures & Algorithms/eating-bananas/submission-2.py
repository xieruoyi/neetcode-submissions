from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        min_h = 1
        max_h = piles[-1]
        ans = max_h

        while min_h <= max_h:
            target = 0
            mid_h = (min_h + max_h) // 2

            for pile in piles:
                target += ceil(pile / mid_h)

            if target <= h:
                ans = mid_h
                max_h = mid_h - 1
            else:
                min_h = mid_h + 1

        return ans