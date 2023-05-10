class Solution:
    def get_max_substring(self, str_var, s):
        max_str_tmp = [str_var[0]]
        max_str = [str_var[0]]
        for x in range(1, len(str_var)):
            max_str_tmp.append(str_var[x])
            if ''.join(max_str_tmp) not in s:
                return ''.join(max_str)
            max_str.append(str_var[x])
        return ''.join(max_str)

    def lengthOfLongestSubstring(self, s: str) -> int:
        set_str = []
        for x in range(len(s)-1):
            if s[x] != s[x+1]:
                set_str.append(s[x])
        srt_str_joint = ''.join(set_str)
        if srt_str_joint in s:
            return len(srt_str_joint)
        max_str = ''
        s_temp = srt_str_joint
        for index in range(len(set_str)):
            max_str_new = self.get_max_substring(s_temp, s)
            max_str = max_str_new if max_str_new> max_str else max_str
            s_temp = s_temp[index+1:]
            if len(s_temp) < len(max_str):
                return len(max_str)
        return len(max_str)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
