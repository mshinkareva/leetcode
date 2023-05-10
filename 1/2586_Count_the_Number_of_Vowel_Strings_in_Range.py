class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        vowelStrings = len([_ for _ in set(words) if _[0] in vowels and _[-1] in vowels])
        if left < vowelStrings <= right:
            return vowelStrings
        return 0


if __name__ == '__main__':
    print(Solution().vowelStrings(["m","qi","ae"], left=1, right=1))
