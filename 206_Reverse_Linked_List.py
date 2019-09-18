# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        first = head
        pri = None
        while first.next != None:
            second = first.next
            first.next = pri
            #print("first ",first.val)
            #print("second ",second.val)
            
            pri = first
            first = second
           
        first.next = pri

        return first