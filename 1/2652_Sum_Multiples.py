class Solution:
    def sumOfMultiples(self, n: int) -> int:

        return sum([_ for _ in range(n+1) if not _ % 3 or not _ % 5 or not _ % 7])


if __name__ == '__main__':
    print(Solution().sumOfMultiples(7))
