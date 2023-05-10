class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print(strs)
        count = len(strs)
        index = 0
        result = []
        while index != count-2:
            for first,second in strs[index], strs[index+1]:
                if first != second:
                    return ''.join(result)
                result.append(first)
            index += 1





if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
