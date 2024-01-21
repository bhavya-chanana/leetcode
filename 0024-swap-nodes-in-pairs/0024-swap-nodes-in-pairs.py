# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr = dummy, head

        # edge case -> curr.next -> so that we have a pair to swap
        while curr and curr.next:
            nxt = curr.next.next
            second = curr.next 

            #swap the adjacent pair
            second.next = curr
            curr.next = nxt
            prev.next = second
        
            #updating ptrs
            prev = curr
            curr = curr.next
            
        return dummy.next
