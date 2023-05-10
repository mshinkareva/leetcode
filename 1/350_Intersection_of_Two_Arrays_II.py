import itertools


class Solution:

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersect = [el for el in nums1 if el in nums2]
        kek = {key: min(nums1.count(key), nums2.count(key)) for key in set(intersect)}
        return list(itertools.chain(*[[key] * val for key, val in kek.items()]))



if __name__ == '__main__':
    print(Solution().intersect(
        [1,2,2,1],
        [2,2]))
