# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next

        print(length)

        m = length - n
        
        prev = None
        curr = head
        for i in range(m):
            prev = curr
            curr = curr.next
        
        if m != 0 and m != length - 1:
            prev.next = curr.next
        elif m == 0:
            head = head.next
        elif m == length - 1:
            prev.next = None
        
        return head
        
