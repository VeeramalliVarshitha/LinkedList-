# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        dummy=ListNode(0)
        newhead=dummy
        curr=head
        stack=[]
        while(curr):
            while(stack and stack[-1].val<curr.val):
                stack.pop()
            stack.append(curr)
            curr=curr.next
        for i in stack:
            newhead.next=i
            newhead=newhead.next
        return dummy.next

