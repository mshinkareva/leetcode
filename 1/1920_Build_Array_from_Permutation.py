class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[_]] for _ in range(0, len(nums))]


if __name__ == '__main__':
    print(Solution().buildArray([0,2,1,5,3,4]))
