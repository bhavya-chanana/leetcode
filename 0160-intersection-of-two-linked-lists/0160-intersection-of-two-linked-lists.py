# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummyA = ListNode(0)
        dummyA.next = headA
        dummyB = ListNode(0)
        dummyB.next = headB

        currA = dummyA
        currB = dummyB
        hashtable = {}

        while currA:
            if currA.next and currA.next not in hashtable:
                hashtable[currA.next] = currA.next.val
            
            currA = currA.next

        while currB:
            if currB.next and currB.next in hashtable:
                tmp = currB.next
                return tmp
            elif currB.next:
                hashtable[currB.next] = currB.next.val

            currB = currB.next

        return None
