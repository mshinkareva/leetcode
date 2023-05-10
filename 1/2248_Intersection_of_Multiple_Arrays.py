class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        # Unpack the first list and the remaining lists into two separate variables
        first_list, *remaining_lists = nums

        # Calculate the intersection using set intersections
        result = set(first_list).intersection(*remaining_lists)

        # Convert the resulting set to a sorted list and return it
        return sorted(result)

if __name__ == '__main__':
    print(Solution().intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))