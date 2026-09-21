# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow and fast pointers until they are equal
        # return true
        slow = head
        fast = head.next
        while (slow and fast and fast.next):
            print(slow.val, fast.val)
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next
        return False