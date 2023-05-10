class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for first, second in zip(s[:-1], s[1:]):
            if s.count(f'{first}{second}') > 1:
                return True
        return False



if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern('abcabcabcabc'))