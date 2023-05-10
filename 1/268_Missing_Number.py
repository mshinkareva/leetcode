class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        generated_list = {el for el in range(len(nums)+1)}
        return (generated_list-set(nums)).pop()

if __name__ == '__main__':
    print(Solution().missingNumber([0,1]))
