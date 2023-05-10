class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int(''.join([str(digit) for digit in digits]))+1
        return [int(d) for d in str(num)]

if __name__ == '__main__':
    print(Solution().plusOne([1,2,3]))
