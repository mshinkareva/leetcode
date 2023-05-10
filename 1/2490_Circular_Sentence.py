class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sent_split: list = sentence.split(' ')
        for _ in range(len(sent_split)-1):
            next = _+1
            if sent_split[_][-1] != sent_split[next][0]:
                return False
        if sent_split[0][0] != sent_split[-1][-1]:
            return False
        return True




if __name__ == '__main__':
    print(Solution().isCircularSentence("Leetcode is cool"))
