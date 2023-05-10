class Solution:
    def findComplement(self, num: int) -> int:
        binary_repr = format(num, 'b')
        return int(''.join(['0' if _ == '1' else '1' for _ in binary_repr]), 2)

if __name__ == '__main__':
    print(Solution().findComplement(5))