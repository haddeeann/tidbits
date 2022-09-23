class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_profit = None
        # do it stupid first
        for b, buy_day in enumerate(prices):
            highest_SELL_day = None
            buy_price = prices[b]
            print(f"buy day is {b} ${buy_price}")
            for s, sell_day in enumerate(prices[b+1:], start=b+1):
                if not highest_SELL_day or prices[s] > highest_SELL_day:
                    highest_SELL_day = prices[s]
                    print(f"SELL day is: {s} ${prices[s]}")
            profit = highest_SELL_day - buy_price
            if not highest_profit or profit > highest_profit:
                highest_profit = profit

        print(hightest_profit)



test = [7,1,5,3,6,4]
s = Solution()
s.maxProfit(test)
