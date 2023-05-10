class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        intersection = set(nums1).intersection(set(nums2))
        if not intersection:
            return -1
        return min(intersection)


if __name__ == '__main__':
    print(Solution().getCommon([1, 2, 3], [-1, 4, 4]))
