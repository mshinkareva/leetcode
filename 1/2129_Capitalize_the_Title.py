class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([_.lower().title() if len(_) > 2 else _.lower() for _ in title.split(' ')])


if __name__ == '__main__':
    print(Solution().capitalizeTitle('First Letter Of Each Word'))
