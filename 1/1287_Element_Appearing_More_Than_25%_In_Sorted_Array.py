from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        len_ = len(arr)
        for _ in arr:
            if arr.count(_) / len_ > 0.25:
                return _


if __name__ == '__main__':
    print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
