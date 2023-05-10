class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))


if __name__ == '__main__':
    print(Solution().isIsomorphic('badc', 'baba'))
