#Sort a linked list in O(n log n) time using constant space complexity.

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l.sort()
        m=ListNode(None)
        n=m
        for i in range(len(l)):
            k=ListNode(l[i])
            m.next=k
            m=m.next
        return n.next
