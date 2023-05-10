import numpy as np


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = [int(i) for i in str(n)]
        return np.prod(np.array(n_list)) - sum(n_list)


if __name__ == '__main__':
    print(Solution().subtractProductAndSum(234))