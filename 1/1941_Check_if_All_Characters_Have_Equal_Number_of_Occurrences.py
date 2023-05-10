class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set({el: s.count(el) for el in set(s)}.values())) == 1


if __name__ == '__main__':
    print(Solution().areOccurrencesEqual("abacbc"))
