# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        length=0
        temp=head
        while temp!=None:
            length=length+1
            temp=temp.next    
        q,r=divmod(length,k)
        ans=[]
        curr=head
        for i in range(k):
            dummy=ListNode(0)
            write=dummy
            for i in range(q+(i<r)):
                if curr:
                    write.next=ListNode(curr.val)
                    write=write.next
                    curr=curr.next
            ans.append(dummy.next)
        return ans
