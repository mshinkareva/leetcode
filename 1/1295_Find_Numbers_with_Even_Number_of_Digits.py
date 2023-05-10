class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return len([_ for _ in nums if not len(str(_)) % 2])


if __name__ == '__main__':
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))
