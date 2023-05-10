class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        set_temp = set(nums1) & set(nums2)
        if set_temp:
            one_digit = min(set_temp)
            return one_digit
        min_1, min_2 = min(nums1), min(nums2)
        return int(f'{min_1}{min_2}' if min_1 < min_2 else f'{min_2}{min_1}')


if __name__ == '__main__':
    print(Solution().minNumber(nums1=[4, 1, 3], nums2=[5, 7]))
