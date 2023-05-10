class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        binary = format(n, 'b')
        odd, even = 0, 0
        for ind, char in enumerate(reversed(binary)):
            if int(char) == 1:
                even += not ind % 2
                odd += ind % 2
        return [even, odd]


if __name__ == '__main__':
    print(Solution().evenOddBit(17))
