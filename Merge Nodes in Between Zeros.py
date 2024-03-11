# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        while(temp.next):
            prev=temp
            if(temp.next.val==0):
                temp=temp.next
            if temp.next:
                temp.val+=temp.next.val
                temp.next=temp.next.next
        prev.next=None
        return head
        
