class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for price in range(len(prices)):
            stock = prices[price]
            profit = 0
            futureStock = price + 1
            while futureStock < len(prices):
                profit = prices[futureStock] - stock
                if profit > 0:
                    maxProfit = max(maxProfit, profit)
                futureStock += 1
        return maxProfit
