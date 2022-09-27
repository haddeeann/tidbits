class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_profit = 0
        # do it stupid first
        cache = None
        for b, buy_price in enumerate(prices):
            highest_price = buy_price
            if not cache or b >= cache:
                for s, sell_price in enumerate(prices[b+1:], start=b+1):
                    if sell_price > highest_price:
                        cache = s
                        highest_price = sell_price
            profit = highest_price - buy_price
            if profit > highest_profit:
                highest_profit = profit

        return highest_profit



test = [2,1,4]
sol = Solution()
sol.maxProfit(test)
