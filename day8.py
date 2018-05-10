#Reverse a singly linked list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, r=head, None
        while p:
            r,p.next,p=p,r,p.next
        return r
