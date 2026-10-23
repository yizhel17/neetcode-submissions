# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        dum = ListNode(0, next=head)

        #find the length of the linked list
        length = 0
        cur = head 

        while cur:
            length += 1
            cur = cur.next
        
        #find the middle node
        mid_node = head
        for _ in range((length - 1) // 2):
            mid_node = mid_node.next
        
        

        #reverse the second half
        sec_fir = mid_node.next

        #cut the connection
        mid_node.next = None
        
        sec_pre = None

        while sec_fir:
            nxt = sec_fir.next
            sec_fir.next = sec_pre
            sec_pre = sec_fir
            sec_fir = nxt
        
        #merge the two halves
        while head and sec_pre:
            head_next = head.next
            sec_next = sec_pre.next
            
            head.next = sec_pre
            sec_pre.next = head_next
            
            head = head_next
            sec_pre = sec_next
