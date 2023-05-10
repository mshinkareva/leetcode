import numpy as np


class Solution:
    def sumZero(self, n: int) -> list[int]:
        np.random.dirichlet(np.ones(n),size=1)


if __name__ == '__main__':
    print(Solution().sumZero(5))
