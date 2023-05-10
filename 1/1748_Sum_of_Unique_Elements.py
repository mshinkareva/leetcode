class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum([_ for _ in nums if nums.count(_) ==1])

if __name__ == '__main__':
    print(Solution().sumOfUnique([1,2,3,2]))