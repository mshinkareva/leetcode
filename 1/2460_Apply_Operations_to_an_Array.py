class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for _ in range(len(nums) - 1):
            if nums[_] != nums[_ + 1]:
                continue
            nums[_], nums[_ + 1] = nums[_] * 2, 0
        count_zero = nums.count(0)
        nums = [el for el in nums if el != 0]
        nums.extend([0 for _ in range(count_zero)])

        return nums


if __name__ == '__main__':
    print(Solution().applyOperations([0, 1]))
