class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        len_b = len(format(max(x, y), 'b'))+10
        binary_x = str(format(x, f'#0{len_b}b'))
        binary_y = str(format(y, f'#0{len_b}b'))
        counter = 0
        print(binary_x, binary_y)
        for one, two in zip(binary_x, binary_y):
            if one != two:
                counter += 1
        return counter



if __name__ == '__main__':
    print(Solution().hammingDistance(680142203, 1111953568))


