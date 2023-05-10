class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        massive = set(list(range(1, len(nums)+1)))
        return list(massive - set(nums))

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([1,1]))