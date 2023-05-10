class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = len([_ for _ in nums if _>0])
        neg = len([_ for _ in nums if _ < 0])
        return max(pos, neg)

if __name__ == '__main__':
    print(Solution().maximumCount([-2,-1,-1,1,2,3]))