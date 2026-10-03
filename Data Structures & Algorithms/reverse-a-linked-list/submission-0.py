# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        cont = True
        l = []
        curr = head
        l.append(curr)
        while cont:
            if curr.next != None:
                l.append(curr.next)
                curr = curr.next
                cont = True
            else:
                cont = False
        print(l)

        for i in range(len(l)-1, 0, -1):
            l[i].next = l[i-1]
        l[0].next = None

        return l[-1]

        
                 

        