
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(nums, reverse=True)[2]

if __name__ == '__main__':
    print(Solution().thirdMax([1,1,2]))