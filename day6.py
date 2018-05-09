#Add the two numbers and return it as a linked list.
'''
class ListNode(object):
  def __init__(self,x):
    self.val=x
    self.next=None
'''
def num(l):
    k=0
    i=0
    while l.next!=None:
        k+=l.val*pow(10,i)
        i+=1
        l=l.next
    k+=l.val*pow(10,i)
    return k
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number=num(l1)+num(l2)
        out=str(number)[::-1]
        ans=ListNode(int(out[0]))
        l=ans
        for i in range(1,len(out)):
            p=ListNode(int(out[i]))
            ans.next=p
            ans=ans.next
        return l
