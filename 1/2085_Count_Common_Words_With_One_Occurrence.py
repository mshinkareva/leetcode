class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        return len([x for x in words2 if words1.count(x) == 1 and words2.count(x) == 1])


if __name__ == '__main__':
    print(Solution().countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
