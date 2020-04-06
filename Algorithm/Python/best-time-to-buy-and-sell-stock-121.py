class Solution:
    def maxProfit(self, prices: []) -> int:
        min_price = [0, prices[0]]
        max_price = [0, prices[0]]
        max_profit = 0
        for index, price in enumerate(prices):
            if price < min_price[1]:
                min_price = [index, price]

            if price >= max_price[1]:
                max_price = [index, price]

            if max_price[0] > min_price[0]:
                if max_price[1] - min_price[1] > max_profit:
                    max_profit = max_price[1] - min_price[1]
            else:
                max_price = [min_price[0], min_price[1]]

        return max_profit

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([2,4,1]))
    print(solution.maxProfit([7,6,4,3,1]))