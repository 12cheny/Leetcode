#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        k=0
        if len(s)>1:
            for i in range(len(s)-1):
                if dict[s[i]]>=dict[s[i+1]]:
                    k+=dict[s[i]]
                else:
                    k-=dict[s[i]]
            k+=dict[s[len(s)-1]]
        else:
            k+=dict[s]
        return k
