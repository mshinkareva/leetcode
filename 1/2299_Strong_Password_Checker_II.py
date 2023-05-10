class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if [first for first, second in zip(password[:-1], password[1:]) if first == second]:
            return False
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(not char.isalnum() for char in password):
            return False
        return True


if __name__ == '__main__':
    print(Solution().strongPasswordCheckerII('zd!&1w!rod7&x+6t(c+^hb2+dgp$@40by0#l#7^v960f%(h8e@aw39jz2ml&5h!)s0^$jfqmwx9'))
