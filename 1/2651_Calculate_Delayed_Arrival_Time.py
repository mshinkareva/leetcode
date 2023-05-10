from datetime import datetime, timedelta


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        hours, minutes = divmod(arrivalTime, 100)
        arrival_dt = datetime.strptime(f'{hours}:{minutes}', '%H:%M')
        delayed_dt = arrival_dt + timedelta(minutes=delayedTime)
        return delayed_dt.hour * 100 + delayed_dt.minute


if __name__ == '__main__':
    print(Solution().findDelayedArrivalTime(15, 5))
