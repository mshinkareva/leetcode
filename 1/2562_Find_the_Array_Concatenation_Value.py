class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        mid = (len(nums) + 1) // 2
        base = [int(f'{x}{y}') for x, y in (zip(nums[:mid - 1], nums[::-1]))]
        if not len(nums) % 2:
            base.append(int(f'{nums[mid-1]}{nums[mid]}'))
        else:
            base.append(nums[mid-1])
        return sum(base)





if __name__ == '__main__':
    print(Solution().findTheArrayConcVal([1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28]))