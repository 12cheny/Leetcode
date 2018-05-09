#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l0=ListNode(None)
        l=l0
        while l1 and l2:
            if l1.val>l2.val:
                l.next=l2
                l=l.next
                l2=l2.next
            else:
                l.next=l1
                l=l.next
                l1=l1.next
        if l1:
            l.next=l1
        else:
            l.next=l2
        return l0.next
