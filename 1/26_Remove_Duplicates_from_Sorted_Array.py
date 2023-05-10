class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # return len(set(nums))
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if (nums[i] == nums[i - 1]):
                nums.pop(i)
        return len(nums)





if __name__ == '__main__':
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
