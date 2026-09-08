class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []
        prev = None
        
        while current != None:
            stack.append(current.val)
            current = current.next
        
        for val in stack:
            new_node = ListNode(val)
            new_node.next = prev
            prev = new_node
        
        return prev