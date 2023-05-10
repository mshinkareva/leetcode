import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target not in nums:
            bisect.insort(nums, target)
        return nums.index(target)

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], target=7))