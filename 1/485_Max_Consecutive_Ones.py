class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        temp_str = [str(_) for _ in nums]
        return len(max(''.join(temp_str).split('0'), key=len))

if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))