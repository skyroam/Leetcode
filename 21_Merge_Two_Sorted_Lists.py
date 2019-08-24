# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: pos = l2
        elif not l2: pos = l1
        elif l1.val <= l2.val: pos = l1
        else: pos = l2
            
        while l1 and l2:
            if l1.val <= l2.val:         
                while l1 and l1.val <= l2.val:
                    temp = l1
                    l1 = l1.next
                temp.next = l2
            else:
                while l2 and l2.val <= l1.val:
                    temp2 = l2
                    l2 = l2.next
                temp2.next = l1
            
        if not l1:
            l1 = l2
        if not l2:
            l2 = l1
        return pos
            