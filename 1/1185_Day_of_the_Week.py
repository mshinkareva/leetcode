import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        return datetime.date(year, month, day).strftime('%A')


if __name__ == '__main__':
    print(Solution().dayOfTheWeek(day=31, month=8, year=2019))
