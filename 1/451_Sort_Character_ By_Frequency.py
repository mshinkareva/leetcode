from collections import Counter
from operator import itemgetter

class Solution:
    def frequencySort(self, s: str) -> str:
        temp_dict = Counter(s)
        sorted_dict = dict(sorted(temp_dict.items(), key=itemgetter(1), reverse=True))
        return ''.join([key*val for key, val in sorted_dict.items()])

if __name__ == '__main__':
    print(Solution().frequencySort('ttttrreee'))