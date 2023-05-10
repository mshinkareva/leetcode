class Solution:
    def arrangeCoins(self, n: int) -> int:
        count, temp_n = 1,  n
        while True:
            temp_n -= count
            if temp_n <= count:
                return count
            count += 1


if __name__ == '__main__':
    print(Solution().arrangeCoins(10))
