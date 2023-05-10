class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum((+ 1 if '++' in X else - 1 for X in operations))


if __name__ == '__main__':
    print(Solution().finalValueAfterOperations(["++X","++X","X++"]))

