class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        target_ord = ord(target)
        ord_list = [ord(_) for _ in letters if ord(_) > target_ord]
        if not ord_list:
            return letters[0]
        if len(ord_list) == 1:
            return chr(ord_list[0])
        diff = [el-target_ord for el in ord_list]
        index_ = diff.index(min(*diff, key=abs))
        return chr(ord_list[index_])

if __name__ == '__main__':
    print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "g"))

