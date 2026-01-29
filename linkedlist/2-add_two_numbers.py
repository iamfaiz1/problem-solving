# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode()
        a = l1
        b = l2

        if not l1:
            return l2
        elif not l2:
            return l1
        
        carry = 0
        while(a and b):
            nw = ListNode()
            temp = a.val +b.val + carry
            nw.val = temp%10
            carry = temp//10
            res.next = nw
            res = res.next
            a = a.next
            b = b.next

        while(a):
            nw = ListNode()
            temp = a.val +carry
            nw.val = temp % 10
            carry = temp //10
            res.next = nw
            res = res.next
            a = a.next

        while(b):
            nw = ListNode()
            temp = b.val +carry
            nw.val = temp % 10
            carry = temp //10
            res.next = nw
            res = res.next
            b = b.next

        if carry !=0:
            res.next = ListNode(carry) 
        return dummy.next
