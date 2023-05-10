import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digits = re.findall(r'\d+', word)
        return len({int(digit) for digit in digits})


if __name__ == '__main__':
    print(Solution().numDifferentIntegers("a1b01c001"))
