

if __name__ == '__main__':
    with open('file.txt') as file:
        print(file.readlines()[9].strip())
