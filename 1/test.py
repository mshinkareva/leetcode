
if __name__ == '__main__':
    def generate_numbers(mask, limit):
        numbers = []

        # Replace '?' with digits from 0 to 9
        for digit in range(10):
            new_mask = mask.replace('?', str(digit))

            # Generate numbers by replacing '*' with any sequence of digits (including empty)
            for i in range(1 + len(str(limit)) - len(new_mask.replace('*', ''))):
                for combination in itertools.product(range(10), repeat=i):
                    num = int(new_mask.replace('*', ''.join(map(str, combination))))
                    if num < limit:
                        numbers.append(num)

        return sorted(numbers)


    import itertools

    mask = '234?5*6'
    limit = 10 ** 8
    numbers = generate_numbers(mask, limit)
    print([f'{_} /211 = {_/211}' for _ in numbers if not _%211])