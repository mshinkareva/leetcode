class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index_1, num_1 in enumerate(nums):
            for index_2, num_2 in enumerate(nums):
                if index_1 == index_2 and num_1 + num_2 == target:
                    continue
                if num_1 + num_2 == target:
                    return [index_1, index_2]


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))
