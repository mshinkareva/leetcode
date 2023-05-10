import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        return set(sentence.lower()) >= alphabet


if __name__ == '__main__':
    print(Solution().checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))

