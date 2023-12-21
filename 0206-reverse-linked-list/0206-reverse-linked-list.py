# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            #next value
            next = curr.next
            # current pointing to previous value -- reversing
            curr.next = prev
            #updating prev and curr to the next value
            prev = curr
            curr = next

        # return prev bc curr would be out of bounds after the last iteration and prev would point to the last element
        return prev
            
     