class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        new_list = {_ for _ in nums if nums.count(_) % 2}
        new_list_len = len(new_list)
        return [int((len(nums)-new_list_len)/2), new_list_len]

if __name__ == '__main__':
    print(Solution().numberOfPairs([0]))
