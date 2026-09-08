class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0
        left = 0
        right = 1
        while left<right and right < len(prices):
            curr_profit = prices[right] - prices[left]
            if(prices[left]>prices[right]):
                left=right
            right=right+1
            max_profit = max(max_profit,curr_profit)
        return max_profit


        