# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        # want to find a way to compare all heads of every
        # lists
        # and get the minimum 
        # whichever is the min we move that pointer
        # to its next pointer -> min_ll = min_ll.next
        # maybe we can do this by add
        # we can have a minheap(that saves)
        # (val, node)
        # so it is sorted by val from lowest to highest
        # at most k length
        # keep going until heap is empty
        # this is assured as when i remove an element from 
        # top val, node =  heappop()
        # then I move to next in that (node = node.next)
        # if node.next != None -> heappush(node.val, node)
        # append val to ans
        # logk for each heap operation
        # 2 logk for push and pop
        # we do this n times
        #2n logk
        # nlogk
        
        minHeap = [] # length k max
        sorted_list = ListNode(0)


        # initialize with head of every list
        for head in lists:
            if head:
                heapq.heappush(minHeap, (HeapNode(head)))
        
        
        cur = sorted_list
        while (minHeap):
            heap_node = heapq.heappop(minHeap)
            node = heap_node.node
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minHeap, HeapNode(node.next))
        cur.next = None  # Set the next of the last node to None

        return sorted_list.next



