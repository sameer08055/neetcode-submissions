# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=head
        b=head
        index=-1
        while b is not None and b.next is not None:
            a=a.next
            b=b.next.next
            if(a==b):
                return True
            
        return False
            

        