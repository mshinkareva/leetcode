class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s2 == s1:
            return True
        diff = []
        for char_1, char_2 in zip(s1, s2):
            if char_2 not in s1 or char_1 not in s2:
                return False
            if s1.count(char_1) != s2.count(char_1):
                return False
            if char_2 != char_1:
                diff.append(char_2)
        if len(diff) == 2:
            return True
        return False


if __name__ == '__main__':
    # print(Solution().areAlmostEqual(s1="djp", s2="pld"))
    # print(Solution().areAlmostEqual(s1="caa", s2="aaz"))
    # print(Solution().areAlmostEqual(s1="kannb", s2="bankb"))
    print(Solution().areAlmostEqual(s1="siyolsdcjthwsiplccjbuceoxmpjgrauocx", s2="siyolsdcjthwsiplccpbuceoxmjjgrauocx"))
