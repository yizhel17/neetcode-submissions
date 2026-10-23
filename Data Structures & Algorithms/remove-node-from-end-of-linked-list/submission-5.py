# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dum = ListNode(0, next=head)
        slow = dum
        fast = head
        
        for _ in range(n): #先让fast走n次
            fast = fast.next
        
        #再让fast走到end,符合题意中 倒数第n个 的pointer manipulation
        while fast:
            slow = slow.next
            fast = fast.next

        #remove the nth node from the END of the list
        slow.next = slow.next.next

        return dum.next
