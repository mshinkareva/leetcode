class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')



if __name__ == '__main__':
    print(Solution().interpret("G()(al)"))