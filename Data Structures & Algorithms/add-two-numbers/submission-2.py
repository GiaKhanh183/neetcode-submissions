# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def translate(self, lst: Optional[ListNode]) -> int:
            cur = lst
            num = 0
            count = 0
            while cur:
                num += cur.val*(10**count)
                cur = cur.next
                count+=1
            return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        cur1 = l1
        cur2 = l2
        
        sums = self.translate(l1) + self.translate(l2)
        node = ListNode()
        if sums == 0:
            return ListNode(0)
        while sums != 0:
            cur.next = ListNode(sums%10)
            sums = sums//10
            cur = cur.next

        return dummy.next 