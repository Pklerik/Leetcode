from typing import List, Tuple

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        sum_profit = 0
        while index < len(prices):
            if index == 0:
                if len(prices) == 1:
                    return 0
                if len(prices) == 2:
                    return prices[1] - prices[0] if prices[1] - prices[0] >= 1 else 0
            else:
                sum_profit += prices[index] - prices[index-1] if prices[index] - prices[index-1] > 0 else 0
            index += 1
        return sum_profit
            

prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))