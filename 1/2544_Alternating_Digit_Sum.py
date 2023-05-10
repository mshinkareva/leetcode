class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = list(str(n))
        return sum([int(el)*((-1)**ind) for ind, el in enumerate(digits)])


if __name__ == '__main__':
    print(Solution().alternateDigitSum(886996))


