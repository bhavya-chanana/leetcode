# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        nth = length - n
        count = 0
        dummy = ListNode(next = head)

        curr = dummy
        while curr:
            # remove nth node
            if count == nth:
                curr.next = curr.next.next
            count += 1
            curr = curr.next

        return dummy.next
        