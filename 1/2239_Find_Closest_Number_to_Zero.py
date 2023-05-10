class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        result = min((abs(x), x) for x in nums)
        return max(x for x in result if x in nums)


if __name__ == '__main__':
    print(Solution().findClosestNumber([2,-1,1]))