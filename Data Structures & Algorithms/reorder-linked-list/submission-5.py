# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head
        # [0 1 2 3 4 5 6]

        def merge_two_lists(l1,l2):
            l1Turn = True
            # dummy = ListNode()
            # dummy.next = l1
            while(l1 and l2):
                if l1Turn:
                    
                    nxtNode = l1.next
                    l1.next = l2
                    l1 = nxtNode
                        
                else:
                    
                    nxtNode = l2.next
                    l2.next = l1
                    l2 = nxtNode
                l1Turn = not l1Turn
            



        # find half way
        slow = head
        fast = head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        cur = slow.next

        slow.next = None
    
        # reverse second half
        prev = None
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        

        # merge 2 lists
        merge_two_lists(head, prev)
        
        
        