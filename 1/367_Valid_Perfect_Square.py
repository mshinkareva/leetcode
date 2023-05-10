class Solution:
    def get_next_approximation(self, x_0, x):
        """Computes the next approximation for the square root of x using x_0 as the previous approximation."""
        return (x_0 + x // x_0) // 2

    def my_sqrt(self, x: int) -> int:
        """Returns the integer square root of x."""
        if x == 0:
            return 0
        if x == 1:
            return 1
        prev_x = x // len(str(x))
        x_0 = self.get_next_approximation(prev_x, x)
        while abs(prev_x - x_0) > 1:
            prev_x = x_0
            x_0 = self.get_next_approximation(x_0, x)
            print(x_0)
        return round(x_0)

    def isPerfectSquare(self, num: int) -> bool:
        return bool(self.my_sqrt(num) ** 2 == num)


if __name__ == '__main__':
    print(Solution().isPerfectSquare(81))
