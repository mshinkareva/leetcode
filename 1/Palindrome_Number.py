class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return False
        reversed_x = int(str(x)[::-1])
        return reversed_x == x


if __name__ == '__main__':
    print(Solution().isPalindrome(0))
