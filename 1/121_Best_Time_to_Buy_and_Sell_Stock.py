class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi = 0
        for buy in prices[:-1]:
            for sell in prices[prices.index(buy):]:
                maxi = sell - buy if sell - buy > maxi else maxi
        return maxi


if __name__ == '__main__':
    print(Solution().maxProfit([7,6,4,3,1]))
