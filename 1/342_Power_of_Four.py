import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else math.log(n, 4) % 1 == 0


if __name__ == '__main__':
    print(Solution().isPowerOfFour(0))
