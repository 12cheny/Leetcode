#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution(object):
    def sum(list):
        m=0
        for i in range(len(lsit)):
            m+=list[i]
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={'[':1,'(':2,'{':3,']':-1,')':-2,'}':-3}
        k=0
        l=[0,]
        if len(s)>=1:
            for i in range(len(s)-1):
                if dict[s[i]]>0:
                    l.append(dict[s[i]])
                if dict[s[i]]<0:
                    if dict[s[i]]+l[len(l)-1]==0:
                        del l[len(l)-1]
                    else:
                        return False
            if dict[s[len(s)-1]]+sum(l)==0:
                return True
            else:
                return False
        else:
            return True
