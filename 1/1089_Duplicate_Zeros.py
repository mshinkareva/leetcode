class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        shift = arr.count(0)

        for i in range(n-1, -1, -1):
            if i + shift < n:
                arr[i + shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                if i + shift < n:
                    arr[i + shift] = 0



if __name__ == '__main__':
    print(Solution().duplicateZeros([1,0,2,3,0,4,5,0]))
