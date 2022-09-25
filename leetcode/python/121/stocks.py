class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_profit = 0
        # do it stupid first
        for b, buy_price in enumerate(prices):
            highest_price = buy_price
            print(f"buy day is {b} ${buy_price}")
            for s, sell_price in enumerate(prices[b+1:], start=b+1):
                if not highest_price or sell_price > highest_price:
                    highest_price = sell_price
                    print(f"SELL day is: {s} ${sell_price}")
            profit = highest_price - buy_price
            if profit > highest_profit:
                highest_profit = profit

        return highest_profit



test = [7,1,5,3,6,4]
sol = Solution()
sol.maxProfit(test)
