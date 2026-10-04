# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # The reversed right half of the list
        rev = prev

        while head.next and rev.next:
            temp1 = head.next
            temp2 = rev.next
            head.next = rev
            rev.next = temp1
            head = temp1
            rev = temp2
                    


