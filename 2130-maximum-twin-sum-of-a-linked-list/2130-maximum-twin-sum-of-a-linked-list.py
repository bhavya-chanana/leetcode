# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        #finding middle of the linkedlist using fast and slow ptrs
        while fast and fast.next:    
            slow = slow.next
            fast = fast.next.next

        #slow pts to the second half of the linkedlist 
        prev = None
        # reversing linkedlist
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        #computing max twin sum
        curr1, curr2 = head, prev
        maxSum = 0
        while curr1 and curr2:
            maxSum = max(maxSum, (curr1.val + curr2.val))
            curr1, curr2 = curr1.next, curr2.next

        return maxSum