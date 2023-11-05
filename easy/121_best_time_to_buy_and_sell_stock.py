class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit,price-min_profit)
            min_profit = min(min_profit, price)
        return max_profit