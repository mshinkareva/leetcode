class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(',', '.')


if __name__ == '__main__':
    print(Solution().thousandSeparator(1234))
