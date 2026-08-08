class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 1
        buyMin = prices[i-1]

        while i < len(prices):
            buyMin = min(buyMin, prices[i-1])
            profit = max(profit, prices[i] - buyMin)
            i += 1

        return profit