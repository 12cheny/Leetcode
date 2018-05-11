#Given a sorted linked list, delete all duplicates such that each element appear only once.

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=head
        if head!=None:
            while head.next:
                if head.val==head.next.val:
                    head.next=head.next.next
                else:
                    head=head.next
        return l
