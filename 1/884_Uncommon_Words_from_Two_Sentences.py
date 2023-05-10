class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1_list = s1.split(' ')
        s2_list = s2.split(' ')
        w1 = [word for word in s1_list if word not in s2_list and s1_list.count(word) == 1]
        w2 = [word for word in s2_list if word not in s1_list and s2_list.count(word) == 1]
        return w1+w2


if __name__ == '__main__':
    print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))
