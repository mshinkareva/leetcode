from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        for rev, basic in zip(reversed(head), head):
            if rev != basic:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isPalindrome([1,2,2,1]))
