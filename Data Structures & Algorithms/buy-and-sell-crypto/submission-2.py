class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float("inf")
        max_profit = 0
        for price in prices:
            if(price<min_price_so_far):
                min_price_so_far = price
            t_profit = price - min_price_so_far
            if(t_profit>max_profit):
                max_profit = t_profit
        return max_profit
        