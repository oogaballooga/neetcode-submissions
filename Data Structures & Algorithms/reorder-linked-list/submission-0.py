# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split linked list in half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse second half
        curr = l2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev

        # combine lists
        dummy = node = ListNode()
        while l2:
            node.next = l1
            l1 = l1.next
            node = node.next
            node.next = l2
            l2 = l2.next
            node = node.next
        
        node.next = l1
