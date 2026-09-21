# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        seems to be ordered as split in 
        2 halves
        1st half asc
        2nd half desc
        merged two list one at time
         strat

        find mid
        left = head O(n/2)
        right = mid O(n/2)
        reverse right O(n/2)
        merge(left, right) O(n)



        can also have traverse through array once to get n
        lets save a prev pointer for the array before tail
        save tail from traverse
        i think i will need a doubly or reverse list
        lets do A1
        save n/2
        res = Node
        for i [0,n/2):
            h = head of list 
            t = tail of list
            
        if nodes leftover add to end (mid)
# '''

#                 find mid
        mid = None
        mid = head
        fast = head
        while (mid and fast and fast.next):
            mid = mid.next
            fast = fast.next.next
        left = head
        print("head")
        # def reverseLL(node):
        prev = None
        cur = mid.next

        mid.next = None
        while(cur):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        # return prev
        # right = reverseLL(mid.next)

        # merge
        # dummy = ListNode()
        # cur = dummy
        # print("hello")
        # while (right):
            
        #     nextLeft, nextRight = left.next, right.next
            
        #     left.next = right
        #     right.next = nextLeft

        #     left, right = nextLeft, nextRight

        #  first, second = head, prev
        right = prev
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2
        # if left:
        #     cur = left
        # if right:
        #     cur = right
        

#         left = head O(n/2)
#         right = mid O(n/2)
#         reverse right O(n/2)
#         merge(left, right) O(n)
