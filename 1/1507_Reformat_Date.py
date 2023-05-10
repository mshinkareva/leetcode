from datetime import datetime


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').split(' ')
        month = datetime.strptime(month, "%b").month
        formatted_date = datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d")
        return formatted_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(Solution().reformatDate("20th Oct 2052"))