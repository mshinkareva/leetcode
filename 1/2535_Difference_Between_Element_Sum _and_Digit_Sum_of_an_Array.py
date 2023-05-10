class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits = []
        for _ in nums:
            for digit in str(_):
                digits.append(int(digit))
        return sum(nums)-sum(digits)

if __name__ == '__main__':
    print(Solution().differenceOfSum([1,15,6,3]))



