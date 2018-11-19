class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n==1):
            return '1'
        strr='11'
        count=1
        while (n > 2):
          str1 = ''
          for i in range(1,len(strr)):
             m=strr[i]
             if(strr[i-1]==m):
                count=count+1
             else:
                str1=str1+str(count)+strr[i - 1]
                count=1
             if (i == (len(strr) - 1)):
                str1 = str1 + str(count) + strr[i]
                break
          count=1
          strr=str1
          n=n-1
        return strr
    if __name__ == '__main__':
        result=countAndSay(4,4)
        print(result)

