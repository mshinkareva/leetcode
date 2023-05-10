class Solution:
    def countBits(self, n: int) -> list[int]:
        bin_num = [bin(num)[2:] for num in range(n + 1)]
        return [sum([int(_) for _ in num]) for num in bin_num]


if __name__ == '__main__':
    print(Solution().countBits(2))
