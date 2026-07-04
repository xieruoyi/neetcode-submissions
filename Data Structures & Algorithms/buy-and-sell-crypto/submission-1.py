class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while j < len(prices):
            profit = max(profit, prices[j]-prices[i])
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
        return profit