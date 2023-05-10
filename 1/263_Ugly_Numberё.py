class Solution:
    def isUgly(self, n: int) -> bool:
        divides = {_ for _ in range(2, (n // 2) + 1) if n % _ == 0}
        return divides.issubset({2, 3, 5})


if __name__ == '__main__':
    print(Solution().isUgly(6))
