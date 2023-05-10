from collections import Counter
class Solution:
    def compress(self, chars: list[str]) -> int:
        temp_dict = Counter(chars)
        new_list = []
        for key, val in temp_dict.items():
            new_list.append(key)
            new_list.append(str(val))
        print(new_list)
        return len(new_list)


if __name__ == '__main__':
    print(Solution().compress(["a","a","b","b","c","c","c"]))