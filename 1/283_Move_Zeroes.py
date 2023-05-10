class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = 0
        while first < len(nums):
            if nums[first] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                second += 1
            first += 1



if __name__ == '__main__':
    num_test = [0,1,0,3,12]
    Solution().moveZeroes(num_test)
    print(num_test)