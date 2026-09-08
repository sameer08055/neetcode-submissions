class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')
        max_profit = 0
        for i in range(0, len(prices)):
            if(prices[i]<min_price_so_far):
                min_price_so_far = prices[i]
            t_profit = prices[i] - min_price_so_far
            if(t_profit>max_profit):
                max_profit = t_profit
        return max_profit
        