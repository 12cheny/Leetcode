#Remove all elements from a linked list of integers that have value val.

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        k=ListNode(None)
        k.next=head
        l=k
        while k.next:
            if k.next.val==val:
                k.next=k.next.next
                if k==None:
                    return l.next
            else:
                k=k.next
        return l.next
