class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        return len([_ for _ in words if s.startswith(_)])

if __name__ == '__main__':
    print(Solution().countPrefixes(["a","b","c","ab","bc","abc"], "abc"))