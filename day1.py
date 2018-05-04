class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=-pow(2,31) and x<=pow(2,31)-1:
            x_str=str(x)
            if x_str[0]=='-':
                k=0
                for i in range(1,len(x_str)):
                    k-=int(x_str[i])*pow(10,i-1)
                if k>=-pow(2,31):
                    return k
                else:
                    return 0
            else:
                k=0
                for i in range(len(x_str)):
                    k+=int(x_str[i])*pow(10,i)
                if k<=pow(2,31)-1:
                    return k
                else:
                    return 0
                
        else:
            return 0
