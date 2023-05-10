class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        return [index for index, num in enumerate(sorted_nums) if num == target]

if __name__ == '__main__':
    print(Solution().targetIndices([1,2,5,2,3], 3))
