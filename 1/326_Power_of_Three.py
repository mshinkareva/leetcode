class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==1:
            return True
        if n < 1:
            return False
        while True:
            mod = n % 3
            if mod:
                return False
            n = n / 3
            if n == 1:
                return True


if __name__ == '__main__':
    print(Solution().isPowerOfThree(15))
