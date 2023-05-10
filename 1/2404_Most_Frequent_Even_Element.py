from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:

        temp_dict = Counter([_ for _ in nums if not _ % 2 or _ == 0])
        even_count = dict(sorted(temp_dict.items()))
        if not even_count:
            return -1
        max_val = max(even_count.values())
        most_frequent_evens = [key for key, val in even_count.items() if val == max_val]
        return min(most_frequent_evens)


if __name__ == '__main__':
    print(Solution().mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
