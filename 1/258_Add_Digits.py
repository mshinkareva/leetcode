class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        num = sum([int(i) for i in str(num)])
        return self.addDigits(num)




if __name__ == '__main__':
    print(Solution().addDigits(9))
