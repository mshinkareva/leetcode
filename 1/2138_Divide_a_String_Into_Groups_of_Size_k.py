class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        temp_str = [s[i:i + k] for i in range(0, len(s), k)]
        return [f'{_ + fill * (k - len(_))}' for _ in temp_str]


if __name__ == '__main__':
    print(Solution().divideString(s="abcdefghik", k=3, fill="x"))
