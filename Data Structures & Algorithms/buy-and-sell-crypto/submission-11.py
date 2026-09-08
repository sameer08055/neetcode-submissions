class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        max_profit = 0
        for i in range(0,len(prices)):
            if(prices[i]<min_so_far):
                min_so_far=prices[i]
            todays_profit = prices[i] - min_so_far
            if(todays_profit>max_profit):
                max_profit = todays_profit
        return max_profit
        