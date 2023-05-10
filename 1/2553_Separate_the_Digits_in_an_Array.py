import itertools


class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        raw = [[int(x) for x in str(num)] for num in nums]
        return list(itertools.chain(*raw))

if __name__ == '__main__':
    print(Solution().separateDigits([13,25,83,77]))