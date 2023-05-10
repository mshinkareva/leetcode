from numpy import prod, array

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        return int(prod(array(nums)))

if __name__ == '__main__':
    print(Solution().maximumProduct([-1,-2,-3]))