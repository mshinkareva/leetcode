# Definition for singly-linked list.
from typing import Optional


class ListNode():
    def __init__(self, val=0, next=None):
        super().__init__()
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        while list1 and list2:
            num_1, num_2 = list1.val, list2.val
            if num_1 > num_2:
                num_1, num_2 = num_2, num_1
            new_list.extend([num_1, num_2])
        return new_list




if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode(1), ListNode(2)))