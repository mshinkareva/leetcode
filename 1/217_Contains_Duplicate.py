class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not len(set(nums)) == len(nums)


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,4]))



