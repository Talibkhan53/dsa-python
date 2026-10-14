class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0 
        max_profit = 0
        min_price = prices[0]
        for price in range(1,len(prices)):
            profit = prices[price]  - min_price 
            max_profit =  max(profit,max_profit)
            min_price = min(prices[price],min_price)
        return max_profit
