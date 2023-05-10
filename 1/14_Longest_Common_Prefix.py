from difflib import SequenceMatcher

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        target = ''
        start = strs[0]
        count = len(strs)

        if count == 1:
            return start
        match = SequenceMatcher(None, start, strs[1]).get_matching_blocks()[0]
        target = start[match.a: + match.size]




if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["abca","aba","aaab"]))
