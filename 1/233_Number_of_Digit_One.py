class Solution:
    def countDigitOne(self, n: int) -> int:
        return ''.join([str(_) for _ in range(n + 1) if str(_).count('1')]).count('1')


if __name__ == '__main__':
    print(Solution().countDigitOne(824883294))
