class Solution:
    def is_self_driving(self, num: int):
        str_num = str(num)
        return all(int(digit) != 0 and num % int(digit) == 0 for digit in str_num)

    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        return [_ for _ in range(left, right+1, 1) if self.is_self_driving(_)]



if __name__ == '__main__':
    print(Solution().selfDividingNumbers(left=1, right=22))
