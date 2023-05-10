class Solution:
    def toHex(self, num: int) -> str:
        trans = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        kek = []
        if num <= 0:
            return bin(num)

        while num:
            lol, num = num % 16, num // 16
            kek.append(f'{lol}') if lol < 10 else kek.append(trans.get(lol))
        kek.reverse()
        return ''.join(kek)


if __name__ == '__main__':
    print(Solution().toHex(0))
