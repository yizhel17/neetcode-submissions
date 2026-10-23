# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        

        #find the middle node
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid_node = slow
        
        #save the second half's first node
        sec_fir = mid_node.next

        #cut the connection
        mid_node.next = None
        
        

        #reverse the second half
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
