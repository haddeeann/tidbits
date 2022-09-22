class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sell = prices[len(prices) - 1]
        i_sell = len(prices) - 1
        min_buy = prices[len(prices) - 1]
        i_buy = len(prices) - 1
        for i, p in enumerate(reversed(prices)):
            if p > max_sell and i_sell < i_buy:
                max_sell = p
                i_sell = i
            if p < min_buy:
                min_buy = p
                i_buy = i


test = [7,1,5,3,6,4]
s = Solution()
s.maxProfit(test)
