import itertools


class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        temp_list = [nums[2*i]*[nums[2*i+1]] for i in range(len(nums)//2)]
        return list(itertools.chain(*temp_list))


if __name__ == '__main__':
    print(Solution().decompressRLElist([1,2,3,4,6,7]))