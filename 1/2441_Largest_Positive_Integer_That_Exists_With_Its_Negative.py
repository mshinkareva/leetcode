class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        for _ in sorted(nums, reverse=True):
            if _*(-1) in nums:
                return _
        return -1


if __name__ == '__main__':
    print(Solution().findMaxK([-1,10,6,7,-7,1]))