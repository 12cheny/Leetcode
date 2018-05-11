#Given a linked list, remove the n-th node from the end of list and return its head.

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l=head
        len=0
        while l:
            len+=1
            l=l.next
        k=head
        if len==n:
            return k.next
        else:
            for i in range(len-n-1):
                head=head.next
            head.next=head.next.next
        return k
