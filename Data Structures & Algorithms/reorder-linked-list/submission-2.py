# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #用中心点来切分成两半
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        se_nde = slow.next
        slow.next = None

        #反转第二部分的链表
        pre = None
        cur = se_nde

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        #合并两个部分成为一个新的链表
        l1 = head
        l2 = pre

        while l1 and l2:
            nxt1 = l1.next
            l1.next = l2
            l1 = nxt1

            nxt2 = l2.next
            l2.next = l1
            l2 = nxt2
