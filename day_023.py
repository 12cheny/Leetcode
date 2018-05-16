#Given a linked list, swap every two adjacent nodes and return its head.

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        k=ListNode(None)
        k.next=head
        l=k
        if k.next!=None:
            while k.next.next:
                j=k.next.val
                k.next.val=k.next.next.val
                k.next.next.val=j
                if k.next.next.next==None:
                    return l.next
                else:
                    k=k.next.next
            return l.next
        else:
            return head
