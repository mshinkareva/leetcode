import operator


class Solution:
    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch][1]

    def repeatedCharacter(self, s: str) -> str:
        occurence = {_ for _ in s if s.count(_) >= 2}
        chars = {char: self.find(s, char) for char in occurence}
        second_index = sorted(chars.items(), key=operator.itemgetter(1))
        return second_index[0][0]


if __name__ == '__main__':
    print(Solution().repeatedCharacter('abccbaacz'))
