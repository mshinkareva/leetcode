from itertools import zip_longest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(pattern)) == len(set(zip_longest(pattern, s))) == len(set(s))

if __name__ == '__main__':
    print(Solution().wordPattern('aba', 'cat cat cat dog'))