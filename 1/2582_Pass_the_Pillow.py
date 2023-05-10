class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person, sing = 1, 1
        for _ in range(time):
            person = n if person + sing == 0 else 1 if person + sing == n + 1 else person + sing
            sing = -sing if person in (n, 1) else sing
        return person


if __name__ == '__main__':
    print(Solution().passThePillow(18, 38))