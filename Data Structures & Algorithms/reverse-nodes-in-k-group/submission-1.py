# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def revLL(head, stop):
            prev = None
            while (head != stop):
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
            return head

        # reverse each k partition and 
        # leave last partition < k as is
        dummy = ListNode(next=head)
        bridge = dummy


        while (head):

            # pointer  traverses start -> start + k
            windowLength = 1

            while (head.next and windowLength < k):
                windowLength +=1
                head = head.next


            if windowLength == k:
            #    1 ->2->
            #    B ->  3 -> 4 5 6
                    # eI ->

                start = bridge.next # 1

                # end node, find the previous BRIDGE NODE; birdge.next = end node
                # 3
                end = head # 3
                if end is not None:
                    nextInterval = end.next #4
                bridge.next = end #3

                # rev LL
                end = revLL(start, nextInterval) 

                # reversing branch
                # edges
                # start node ; link start.next to None save to become the BRIDGE next interval  
                start.next = nextInterval
                bridge = start
                head = nextInterval


            else:
                # leave last partition < k as is
                break
                

        return dummy.next