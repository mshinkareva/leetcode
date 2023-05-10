class Solution:

    def isMonotonic(self, nums: list[int]) -> bool:
        direction = 0
        print(nums[:-1])
        print(nums[1:])
        for a, b in zip(nums[:-1], nums[1:]):
            diff = b - a
            if diff != 0 and direction == 0:
                direction = diff
            if direction * diff < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isMonotonic([1, 2, 2, 3]))
