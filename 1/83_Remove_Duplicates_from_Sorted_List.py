from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            print(current.val)
            kek = head
        return head

if __name__ == '__main__':
    print(Solution().deleteDuplicates(ListNode([1,1,2,3,3])))