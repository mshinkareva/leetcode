class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(_) for _ in accounts])

if __name__ == '__main__':
    print(Solution().maximumWealth([[1,5],[7,3],[3,5]]))