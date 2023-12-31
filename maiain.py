class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            self.reverseList(head.next)    
            head.next.next= head
        head.next = None

        return newHead    
