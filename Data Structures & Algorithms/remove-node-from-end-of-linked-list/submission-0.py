# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        find the nth node from the end
        reassing n =len - n
        remove
            we need the n-1 node link to
            n+1 node

            case 1:
                middle, n-1 to n+1
                return head
            case 2:
                last node, no n+1 node
                    make n-1 -> none
                return head
            case 3:
                first node n=0, no n-1 node
                make sure we return the new head
            case 4:
                only node return None
        '''
        cur = head
        ct = 0
        while(cur):
            ct +=1
            cur = cur.next
        if ct == 1:
            return None
        n = ct - n
        if n == 0:
            return head.next
        cur = head
        prev = None
        i = 0
        while(cur):
            if i == n:
                # print("")
                if cur.next:
                    prev.next = cur.next
                else:
                    prev.next = None
                break
            i+=1
            prev = cur
            cur=cur.next

        return head
        




