class Solution:
    def checking_happy(self, num):
        return sum([int(number) ** 2 for number in str(num)])

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        next_num=None

        while next_num != n or next_num !=1:
            next_num = self.checking_happy(n)
            return self.checking_happy(n)




if __name__ == '__main__':
    print(Solution().isHappy(2))
