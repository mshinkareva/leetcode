class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))