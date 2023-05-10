from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new = [k for k, v in Counter(nums).items() if v == 1]
        return new[0]


if __name__ == '__main__':
    print(Solution().singleNumber([4,1,1,2,1,2,5,5,7,7,8,8,8]))
