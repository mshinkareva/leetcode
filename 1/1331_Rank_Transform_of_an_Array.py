class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        min_ = min(arr)
        return [_//min_ for _ in arr]

if __name__ == '__main__':
    print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))