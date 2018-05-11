#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=[]
        k=ListNode(None)
        k.next=head
        out=k
        if  head==None:
            return head
        else:
            while k.next:
                if k.next.next:
                    if k.next.val==k.next.next.val:
                        l.append(k.next.val)
                        k.next=k.next.next.next
                    elif k.next.val in l:
                        k.next=k.next.next
                    else:
                        k=k.next
                else:
                    if k.next.val in l:
                        k.next=None
                    else:
                        k=k.next
            return out.next
            
