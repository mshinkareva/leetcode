class Solution:
    def get_fizz_buzz(self, number: int) -> str:
        if not number % 3 and not number % 5:
            return 'FizzBuzz'
        if not number % 3:
            return 'Fizz'
        if not number % 5:
            return 'Buzz'
        return str(number)

    def fizzBuzz(self, n: int) -> list[str]:
        return [self.get_fizz_buzz(_) for _ in range(1, n + 1)]


if __name__ == '__main__':
    print(Solution().fizzBuzz(5))
