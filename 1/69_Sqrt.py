import math


class Solution:
    def get_x(self, x_0, x):
        return (x_0 + x / x_0) / 2

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        prev_x = (x / (len(str(x))))
        x_0 = self.get_x(prev_x, x)
        while prev_x - x_0 > 0.01:
            prev_x = x_0
            x_0 = self.get_x(x_0, x)
        return math.floor(x_0)


if __name__ == '__main__':
    print(Solution().mySqrt(20))
