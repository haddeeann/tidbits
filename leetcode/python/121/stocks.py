class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_profit = 0
        highest_sell_price = prices[0]
        cache = None
        for b, buy_price in enumerate(prices):
            if not cache or b >= cache:
                for s, sell_price in enumerate(prices[b+1:], start=b+1):
                    if sell_price > highest_sell_price:
                        cache = s
                        highest_sell_price = sell_price
            profit = highest_sell_price - buy_price
            if profit > highest_profit:
                highest_profit = profit

        return highest_profit


test_cases = [
    {
        "no": 1,
        "input": [7,1,5,3,6,4],
        "answer": 5
    },
    {
        "no": 2,
        "input": [2,1,4],
        "answer": 3
    }
]

sol = Solution()
for x in test_cases:
    answer = sol.maxProfit(x["input"])
    if answer == x["answer"]:
        print(f"answer {x['no']} is correct")
    else:
        print(f"answer {x['no']} is WRONG")
