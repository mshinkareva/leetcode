class Solution:
    def minimize(self, nums):
        sorted_ = list(sorted(set(nums)))
        min_ = sorted_[1] if 0 in nums else sorted_[0]
        return [el - min_ if not el - min_ < 0 else 0 for el in nums]

    def minimumOperations(self, nums: list[int]) -> int:
        if nums == [0]:
            return 0
        if len(nums) == 1:
            return 1
        count = 0
        while True:
            if set(nums) == {0}:
                return count
            nums = self.minimize(nums)
            count += 1


if __name__ == '__main__':
    print(Solution().minimumOperations([7,28,34,76]))
