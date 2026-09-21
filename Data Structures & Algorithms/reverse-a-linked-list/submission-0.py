# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        #   h
        # # 0 1 2 3 none
        #       p c
        while (cur is not None):
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
            
        return prev
        # prev is still at last node return prev