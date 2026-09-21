# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        res = ListNode()
        cur_res = res

        carry = 0

        while (cur1 is not None or cur2 is not None or carry):
            # if a digit is Null, represent as 0
            digit1 = 0 if cur1 is None else cur1.val
            digit2 = 0 if cur2 is None else cur2.val
            #Add the two digits
            digit_sum = digit1 + digit2 + carry
            
            # take number - 10 and save in res
            # add a carry bit
            carry = digit_sum // 10
            cur_res.next = ListNode(digit_sum % 10)


            # iterate to next node in each list
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            cur_res = cur_res.next

            

        return res.next