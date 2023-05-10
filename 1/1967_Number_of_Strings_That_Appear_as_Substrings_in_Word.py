class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return len({el for el in patterns if el in word})


if __name__ == '__main__':
    print(Solution().numOfStrings(["a", "abc", "bc", "d"], "abc"))
