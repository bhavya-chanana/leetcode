# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        curr = head

        while curr:
            if curr.val == val:
                # prev doesnt get updated to curr, because curr.val = val and we need to remove it from the linked list, and curr gets updated to curr.next to go to the next iteration -- thus continue is there
                prev.next = curr.next
                curr = curr.next
                continue
            prev = curr
            curr = curr.next
            
        # return the head of the updated linkedlist 
        return dummy.next