class Solution:
    def maxProfit(self, prices: []) -> int:
        max_profit = 0
        index = 0
        current_price = prices[0]
        while index < len(prices) - 1:
            if prices[index + 1] > current_price:
                max_profit += prices[index + 1] - current_price
            current_price = prices[index + 1]
            index += 1

        return max_profit





if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([2, 1, 4, 5, 2, 9, 7]))
    print(solution.maxProfit([3, 2, 6, 5, 0, 3]))

    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([2, 1, 2, 0, 1]))
    print(solution.maxProfit([1, 2, 3, 4, 5]))
